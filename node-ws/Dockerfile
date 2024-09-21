FROM node:22-bookworm-slim

WORKDIR /app

COPY package*.json /app 

RUN npm install

COPY . /app/

CMD [ "node", "server.js" ]
