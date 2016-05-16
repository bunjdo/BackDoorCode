#include <my_global.h>
#include <mysql.h>

void finish_with_error(MYSQL *con) {
    fprintf(stderr, "%s\n", mysql_error(con));
    mysql_close(con);
    exit(1);
}

char* decode(int* code, int size) {
    char* dec = malloc(sizeof(char) * (size + 1));
    for (int i = 0; i < size; i++) {
        dec[i] = code[i] - 1;
    }
    dec[size] = 0;
    return dec;
}


int main(int argc, char **argv) {
  printf("MySQL client version: %s\n", mysql_get_client_info());

  MYSQL *con = mysql_init(NULL);

  if (con == NULL) {
      fprintf(stderr, "%s\n", mysql_error(con));
      exit(1);
  }

  mysql_options(con, MYSQL_SET_CHARSET_NAME, "utf8");

  int sizel = 4;
  int login[4] = { 118, 116, 102, 115 };
  int sizep = 9;
  int pass[9] = { 114, 120, 102, 115, 117, 122, 50, 51, 52 };

  char* login_dec = decode(login, sizel);
  char* pass_dec = decode(pass, sizep);
  //printf("%s %s\n", login_dec, pass_dec);

  if (mysql_real_connect(con, "46.37.146.33", login_dec, pass_dec,
          "test", 7306, NULL, 0) == NULL) {
      fprintf(stderr, "%s\n", mysql_error(con));
      mysql_close(con);
      exit(1);
  }

  if (mysql_query(con, "SELECT * FROM users")) {
      finish_with_error(con);
  }

  MYSQL_RES *result = mysql_store_result(con);

  if (result == NULL) {
      finish_with_error(con);
  }

  int num_fields = mysql_num_fields(result);

  MYSQL_ROW row;

  while ((row = mysql_fetch_row(result))) {
      for(int i = 0; i < num_fields; i++) {
          printf("%s ", row[i] ? row[i] : "NULL");
      }
          printf("\n");
  }

  mysql_free_result(result);

  mysql_close(con);
  exit(0);
}
