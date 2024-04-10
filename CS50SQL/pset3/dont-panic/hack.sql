UPDATE users
SET
    password = '982c0381c279d139fd221fce974916e7'
WHERE
    username = 'admin';

delete from user_logs where type = update AND 
