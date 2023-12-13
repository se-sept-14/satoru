FROM node:20-alpine3.19 as builder
WORKDIR /vite
COPY package*.json .
RUN npm install
COPY . .
RUN npm run build

FROM node:20-alpine3.19
RUN npm install --global serve
WORKDIR /dist
COPY --from=builder /vite/dist .