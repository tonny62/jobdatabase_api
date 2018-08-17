SELECT
	count AS 'value',
    majornameEN AS 'label_EN',
    majornameTH AS 'label_TH'
FROM major
LEFT JOIN
	(
	SELECT majorid, count(majorid) AS count FROM
		(
		SELECT jobid FROM job
		WHERE job.postdate < '2018-06-15' AND job.postdate > '2018-06-10'
		) AS temp
	LEFT JOIN job_has_major
	ON temp.jobid = job_has_major.jobid
	GROUP BY majorid
	) AS temp2
ON temp2.majorid = major.majorid
LEFT JOIN faculty
ON faculty.facultyid = major.facultyid
