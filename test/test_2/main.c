extern void hello(const char *s);

int main(int argc, char *argv[]) {
    for (int i = 1; i < argc; i++)
    	hello(argv[i]);
    return 0;
}
