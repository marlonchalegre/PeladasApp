# Base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

RUN apk add g++ make py3-pip

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Vue.js project
# RUN npm run build

# Expose the port
EXPOSE 8080

# Start the application
CMD [ "npm", "start"]
