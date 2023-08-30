const { createQueue } = require('kue');

const queue = createQueue();

const objJob = {
  phoneNumber: '52414',
  message: 'This is job message'
};

const job = queue.create('push_notification_code', objJob).save();

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`));
job.on('complete', () => console.log('Notification job completed'));
job.on('failed', () => console.log('Notification job failed'));
