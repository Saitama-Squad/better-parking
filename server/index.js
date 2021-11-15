const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

app.get("/status", (request, response) =>
    response.json({ clients: clients.length })
);

const PORT = process.env.PORT || 5005;

let kafkaData;
let clients = [];

app.listen(PORT, () => {
    console.log(`Facts Events service listening at http://localhost:${PORT}`);
});

const eventsHandler = (request, response, next) => {
    const clientId = Date.now();
    const origin = request.get("origin");
    console.log(origin);
    console.log(`${clientId} Connection open`);
    const headers = {
        "Content-Type": "text/event-stream",
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Credentials": true,
        Connection: "keep-alive",
        "Cache-Control": "no-cache",
    };
    response.writeHead(200, headers);

    const data = `data: ${JSON.stringify(kafkaData)}\n\n`;

    response.write(data);

    const newClient = {
        id: clientId,
        response,
    };

    clients.push(newClient);

    request.on("close", () => {
        console.log(`${clientId} Connection closed`);
        clients = clients.filter((client) => client.id !== clientId);
    });
};

app.get("/events", eventsHandler);

const sendEventsToAll = (newFact) => {
    clients.forEach((client) =>
        client.response.write(`data: ${JSON.stringify(newFact)}\n\n`)
    );
};

const addFact = async (request, respsonse, next) => {
    const newFact = request.body;
    console.log(request.body);
    kafkaData = newFact;
    respsonse.json(kafkaData);
    sendEventsToAll(kafkaData);
    return;
};

app.post("/fact", addFact);
