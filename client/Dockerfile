# Use Node.js v18 image as the base
FROM node:18 as build

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies for production
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the Vue app for production
RUN npm run build

# Use nginx as production server
FROM nginx:1.25-alpine

# Copy the built app from the previous stage to the Nginx directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]