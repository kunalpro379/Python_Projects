class JobSeq:
    class Job:
        def __init__(self, id, deadline, profit):
            self.id = id
            self.deadline = deadline
            self.profit = profit

    @staticmethod
    def comp(max_job, min_job):
        return max_job.profit > min_job.profit

    def job_scheduling(self, jobs):
        jobs.sort(key=lambda x: x.profit, reverse=True)
        max_time = max(job.deadline for job in jobs)
        profit = 0
        job_done = 0
        time_slots = [-1] * (max_time + 1)

        for job in jobs:
            for k in range(job.deadline, 0, -1):
                if time_slots[k] == -1:
                    time_slots[k] = job.id
                    profit += job.profit
                    job_done += 1
                    break

        return job_done, profit

def main():
    job_seq = JobSeq()

    jobs = [
        JobSeq.Job(1, 4, 20),
        JobSeq.Job(2, 1, 10),
        JobSeq.Job(3, 1, 40),
        JobSeq.Job(4, 1, 30),
        JobSeq.Job(2, 4, 20),
        JobSeq.Job(1, 1, 10),
        JobSeq.Job(5, 1, 40),
        JobSeq.Job(5, 1, 70)
    ]

    result = job_seq.job_scheduling(jobs)

    print("Number of jobs scheduled:", result[0])
    print("Total profit gained:", result[1])

    print("Job Sequence:", end=" ")
    for i in range(result[0]):
        if i > 0:
            print("--->", end=" ")
        print(jobs[i].id, end=" ")
    print()

if __name__ == "__main__":
    main()
