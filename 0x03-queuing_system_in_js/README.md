# 0x03. Queuing System in JS

## Description

This project involves creating a queuing system using JavaScript, ES6, Redis, NodeJS, ExpressJS, and Kue. It is part of the ALX Software Engineering curriculum.

## Table of Contents

- [Description](#description)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Tasks](#tasks)
- [Resources](#resources)
- [Author](#author)

## Learning Objectives

By the end of this project, you should be able to explain:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with NodeJS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements

- Your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- Use the `.js` extension for your code

## Setup Instructions

1. **Install Redis:**

   ```sh
   wget http://download.redis.io/releases/redis-6.0.10.tar.gz
   tar xzf redis-6.0.10.tar.gz
   cd redis-6.0.10
   make
   src/redis-server &
   ```

2. **Verify Redis Installation:**

   ```sh
   src/redis-cli ping
   ```

3. **Install NodeJS and npm packages:**

   ```sh
   npm install
   ```

## Tasks

1. **Install a Redis instance**
2. **Node Redis Client**
3. **Node Redis client and basic operations**
4. **Node Redis client and async operations**
5. **Node Redis client and advanced operations**
6. **Node Redis client publisher and subscriber**
7. **Create the Job creator**
8. **Create the Job processor**
9. **Track progress and errors with Kue: Create the Job creator**
10. **Track progress and errors with Kue: Create the Job processor**
11. **Writing the job creation function**
12. **Writing the test for job creation**
13. **In stock?**
14. **Can I have a seat?**

## Resources

- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://redis.io/topics/clients)
- [Redis client for NodeJS](https://github.com/NodeRedis/node-redis)
- [Kue deprecated but still used in the industry](https://github.com/Automattic/kue)

## Author

Tariq Omer, student at ALX Software Engineering
