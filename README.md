# INSTALLATION

Install the handle package

```(bash)
# yum install handle-server
# cd /opt/handle-server
```

Edit the credentials in db/00_database.sql

```(bash)
# vi db/00_database.sql
# cat db/*.sql | mysql -u root -p
```

Create a configuration file (and set the right IP and mysql credentials)

```(bash)
# cat > svr_1/config.dct <<EOF
{
"hdl_http_config" = {
"bind_address" = "<<YOUR_IP>>"
"num_threads" = "15"
"bind_port" = "8000"
"backlog" = "5"
"log_accesses" = "yes"
}

"server_type" = "server"
"hdl_udp_config" = {
"bind_address" = "<<YOUR_IP>>"
"num_threads" = "15"
"bind_port" = "2641"
"log_accesses" = "yes"
}

"hdl_tcp_config" = {
"bind_address" = "<<YOUR_IP>>"
"num_threads" = "15"
"bind_port" = "2641"
"backlog" = "5"
"log_accesses" = "yes"
}

"no_udp_resolution" = "y"
"interfaces" = (
"hdl_udp"
"hdl_tcp"
"hdl_http"
)

"server_config" = {
"storage_type" = "sql"
"sql_settings" = {
  "sql_url" = "jdbc:mysql://localhost/handle"
  "sql_driver" = "com.mysql.jdbc.Driver"
  "sql_login" = "handle"
  "sql_passwd" = "<<YOUR_PWD>>"
  "sql_read_only" = "no"
}
"server_admins" = (
"300:0.NA/1854"
)

"replication_admins" = (
"300:0.NA/1854"
)

"max_session_time" = "86400000"
"this_server_id" = "1"
"max_auth_time" = "60000"
"backup_admins" = (
"300:0.NA/1854"
)

"case_sensitive" = "no"
}

}
EOF
```

Start the handle-server

```(bash)
# service handle-server start
# service handle-server status
```

Test the connection

```(bash)
# lynx http://localhost:8000
```
