from agent import generate_answer

def main():
    print("Welcome to the US Government Document Assistant.")
    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        answer = generate_answer(query)
        print("\nAnswer:\n", answer)

if __name__ == "__main_exit_":
    main()