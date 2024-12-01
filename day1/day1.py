import os.path
from collections import Counter

    
def main():
    ## part 1 : compute total distance
    filename = "input_day1.txt"
    if not os.path.isfile(filename):
        print("Input file does not exist")
    else:
        with open(filename) as f:
            content = f.read().splitlines()
            content = [line.split() for line in content]
            transposed_content = list(map(list, zip(*content)))
            left_list = list(map(int, transposed_content[0]))
            right_list = list(map(int, transposed_content[1]))
            left_list.sort()
            right_list.sort()
            distances = [abs(right_id - left_id) for right_id, left_id in zip(right_list, left_list)]
            total_distance = sum(distances)
            print(total_distance)    
    
    ## part 2 : compute similarity score
            scores = []
            left_counter = Counter(left_list)
            right_counter = Counter(right_list)
            for id, nb_occurrences_in_left_list in left_counter.items() :
                nb_occurrences_in_right_list = right_counter.get(id, 0)
                score = nb_occurrences_in_left_list * (id * nb_occurrences_in_right_list)
                scores.append(score)
            similarity_score = sum(scores)
            print(similarity_score)       
            

if __name__ == "__main__":
    main()