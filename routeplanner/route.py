import heapq
import math

def Euclidean_distance(intersect1, intersect2):
    return math.sqrt((intersect2[0] - intersect1[0])**2 + (intersect2[1] - intersect1[1])**2)
    


def findPath(predecessor, goal,start):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessor[current]
    path.append(start)
    path.reverse()#To print from start -> goal
    return path

def shortest_path(M, start, goal):
    OpenSet = []
    CameFrom = {} 
    Gscore = {}  
    
    CameFrom[start] = None 
    Gscore[start] = 0
    
    heapq.heappush(OpenSet, (0, start))
    
    while len(OpenSet) > 0:
        current = heapq.heappop(OpenSet)[1] 
        
        if current == goal:
            return findPath(CameFrom, current, start)
            
        
        for neighbor in M.roads[current]:
            
            score = Gscore[current] + Euclidean_distance(M.intersections[current], M.intersections[neighbor])
            
            if neighbor not in Gscore or score < Gscore[neighbor]:
                CameFrom[neighbor] = current
                Gscore[neighbor] = score
                
                if neighbor not in OpenSet:
                    heapq.heappush(OpenSet, (score, neighbor))                    
    return 
