'''
Author: Evan Zhuo
KUID: 3109819
Date: 11/13/2024
Lab: lab08
Last modified: 11/18/2024
Purpose: MinHeap Class
'''
#minheap.py [UNUSED]

class MinHeap:
    def __init__(self):
        #Initial Variables
        self._heap = []

    #Add Function
    def add(self, entry):
        self._heap.append(entry)
        #Upheap Entry
        self._upheap(len(self._heap) - 1)

    #Upheap Function
    def _upheap(self, index):
        #Base Case
        if index == 0:
            return
        #Initial Variables
        self_node = self._heap[index]
        parent_index = (index - 1) // 2
        parent_node = self._heap[parent_index]

        #Base Case for Multiple Nodes
        #Compare Current Node with Parent Node
        if self_node >= parent_node:
            return
        else:
            #Swap Positions
            replace_value = self._heap[parent_index]
            self._heap[parent_index] = self._heap[index]
            self._heap[index] = replace_value

            #Recursive Function
            self._upheap(parent_index)

    #Remove Function
    def remove(self):
        #Set Current Root as top_value
        top_value = self._heap[0]
        #Set Last Value as Root and Remove Last Value
        self._heap[0] = self._heap[-1]
        self._heap.pop(-1)
        #Downheap Root
        self._downheap(0)
        #Return Previous top_value
        return top_value

    #Downheap Function
    def _downheap(self, index):
        #Initial Variables
        left_index = 2*index + 1
        right_index = 2*index + 2
        left_gate = False
        right_gate = False
        
        #Toggle Gates
        if left_index <= len(self._heap)-1:
            #toggle left check
            left_gate = True
        if right_index <= len(self._heap)-1:
            #toggle right check
            right_gate = True
            
        #Both Left and Right Gate are off
        if left_gate == False and right_gate == False:
            #No Need to Downheap
            return
        
        #Both Left and Right Gate are on
        elif left_gate == True and right_gate == True:
            #Both child is greater than current value
            if self._heap[index] < self._heap[left_index] and self._heap[index] < self._heap[right_index]:
                #No Need to Downheap
                return
            
            #Check if Left Node or Right Node is Less
            elif self._heap[left_index] <= self._heap[right_index]:
                next_index = left_index
            else:
                next_index = right_index
        
        #Only Left Gate is on
        elif left_gate == True:
            if self._heap[index] <= self._heap[left_index]:
                #No Need to Downheap
                return
            else:
                next_index = left_index

        #Only Right Gate is on
        elif right_gate == True:
            if self._heap[index] <= self._heap[right_index]:
                #No Need to Downheap
                return
            else:
                next_index = right_index

        #Swap Positions
        replace_value = self._heap[next_index]
        self._heap[next_index] = self._heap[index]
        self._heap[index] = replace_value
        
        #Recursive Function
        self._downheap(next_index)