import { createQueue } from 'kue';
import { expect } from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job';

const queue = createQueue();

describe('createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should create a new job', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(1);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
  });

  it('should process the job', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
    ];
    createPushNotificationsJobs(jobs, queue);
    queue.process('push_notification_code_3', (job, done) => {
      expect(job.data).to.eql(jobs[0]);
      done();
    });
    done();
  });
});
