/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) {
            return a->val > b->val;  // min heap
        }
    };

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, Compare> minHeap;
        
        // Initialize: add first node of each list
        for (ListNode* list : lists) {
            if (list != nullptr) {
                minHeap.push(list);
            }
        }
        
        // Create dummy node
        ListNode* dummy = new ListNode(0);
        ListNode* current = dummy;
        
        // Process all nodes
        while (!minHeap.empty()) {
            ListNode* smallest = minHeap.top();
            minHeap.pop();
            
            current->next = smallest;
            current = smallest;
            
            if (smallest->next != nullptr) {
                minHeap.push(smallest->next);
            }
        }
        
        return dummy->next;
    }
};