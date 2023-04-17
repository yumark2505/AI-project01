def readFile(id):
    filename = f"INPUT_{id}.txt"
    f = open(filename, "r")
    capacity = int(f.readline())
    num_class = int(f.readline())
    weight_list = f.readline().split(", ")
    weight_list = [float(x) for x in weight_list]
    value_list = f.readline().split(", ")
    value_list = [int(x) for x in value_list]
    class_label = f.readline().split(", ")
    class_label = [int(x) for x in class_label]
    return capacity, num_class, weight_list, value_list, class_label

class BruteForce:
    def __init__(self, id):
        self.cap, self.num_class, self.weights, self.values, self.labels = readFile(id)
        self.highestVal = 0
    
    def check(self):
        print(self.cap)
        print(self.num_class)
        print(self.weights)
        print(self.values)
        print(self.labels)
    
    def algo(self):
        track = [0]*len(self.labels)
        best_track = [0]*len(self.labels)
        calW, calValue, index = 0, 0, 0
        best_track = self.bruteForce(0 ,track, best_track, calW, calValue, index)
        return best_track
    
    def bruteForce(self,count_class, track, best_track, calW, calValue, index):
        count_class = len(set(self.labels[i] for i in range(len(self.labels)) if track[i] == 1))
        if( calValue > self.highestVal and count_class == self.num_class): 
                self.highestVal = calValue
                best_track = track[:] #copy member
        
        if(index == len(self.weights) or calW > self.cap): 
            return best_track
        
        if(calW + self.weights[index] <= self.cap):
            track[index] = 1
            best_track = self.bruteForce(count_class, track, best_track, calW + self.weights[index], calValue + self.values[index], index + 1)
            track[index] = 0
         
        best_track = self.bruteForce(count_class, track, best_track, calW , calValue, index + 1)
        return  best_track

def main():
    BFS = BruteForce(1)
    BFS.check()
    track = BFS.algo();
    print("Highest val:", BFS.highestVal)
    print(track)

if __name__ == '__main__':
    main()
