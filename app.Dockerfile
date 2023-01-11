FROM node:19-alpine as builder
WORKDIR /app
COPY ./src/neutralisation-app/package.json .
COPY ./src/neutralisation-app/package-lock.json .
RUN npm install
COPY ./src/neutralisation-app .
RUN npm run build
RUN rm .env

FROM nginx:1.23
WORKDIR /usr/share/nginx/html
RUN rm -rf ./*
COPY --from=builder /app/build .
ENTRYPOINT ["nginx", "-g", "daemon off;"]