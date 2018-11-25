FROM node:8

WORKDIR /usr/app/src

COPY package.json ./
RUN yarn install

COPY . .
CMD ["npm", "run", "dev"]
EXPOSE 8080
