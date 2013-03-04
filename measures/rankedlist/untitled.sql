add jar s3n://netflix-dataoven-prod/genie/jars/dataoven-hive-tools.jar;
create temporary function rank as 'com.netflix.hadoop.hive.udf.generic.GenericUDFRank';

SELECT collect_set(id1), collect_sec(id2)
FROM 
(
    SELECT 1 AS dummy, rank, account_id as id1
    FROM users_rank
    WHERE dateint=20130213 
    ORDER BY rank desc 
    LIMIT 10
) A
JOIN 
(
    SELECT1 AS dummy, rank, account_id as id2
    FROM 
    (
        SELECT account_id as ID2, score
        FROM prod_green_70178217_newusers_ranks
        WHERE dateint=20130213
        SORT BY score DESC
        LIMIT 10
    ) a
) B
ON (A.rank = B.rank)
GROUP BY dummy;

add jar CollectAll.jar;
create temporary function CollectAll as 'com.example.CollectAll';
    
SELECT l1, l2
FROM 
(
    SELECT runid, CollectAll(MAP(rank, account_id)) as ld1
    FROM users_rank
    WHERE runid=20130213
    GROUP BY runid
    LIMIT 10

) A
JOIN
(
    SELECT dateint, CollectAll(MAP(rank, account_id)) as rank, account_id
    FROM 
    (
        SELECT dateint, score, account_id 
        FROM prod_green_70178217_newusers_ranks 
        order by score desc limit 10
    ) a
    GROUP BY dateint
) B
ON (A.runid = B.dateint)



