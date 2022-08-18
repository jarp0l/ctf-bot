CREATE TABLE IF NOT EXISTS members (
  serial_num SERIAL NOT NULL,
  member_id BIGINT PRIMARY KEY,
  server_nickname TEXT NOT NULL,
  added_on TIMESTAMP NOT NULL,
  message_id BIGINT NOT NULL
);
CREATE TABLE IF NOT EXISTS challenges (
  challenge_id SERIAL PRIMARY KEY,
  author_id BIGINT REFERENCES members(member_id),
  added_on TIMESTAMP NOT NULL,
  category TEXT NOT NULL,
  challenge_description TEXT NOT NULL,
  messsage_id BIGINT NOT NULL
);
CREATE TABLE IF NOT EXISTS flags (
  challenge_id INT PRIMARY KEY REFERENCES challenges(challenge_id) ON DELETE CASCADE,
  added_on TIMESTAMP NOT NULL,
  flag TEXT NOT NULL,
  message_id BIGINT NOT NULL
);
CREATE TABLE IF NOT EXISTS solvers (
  challenge_id INT PRIMARY KEY REFERENCES flags(challenge_id),
  member_id BIGINT REFERENCES members(member_id),
  solved_on TIMESTAMP,
  message_id_on_success BIGINT
);
CREATE TABLE IF NOT EXISTS submissions (
  serial_num SERIAL,
  challenge_id INT REFERENCES flags(challenge_id),
  member_id BIGINT NOT NULL REFERENCES members(member_id),
  submitted_flags TEXT NOT NULL,
  added_on TIMESTAMP NOT NULL,
  message_id BIGINT NOT NULL
);