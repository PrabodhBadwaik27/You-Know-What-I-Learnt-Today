public class LinkedListII {
	public Node head = null;
	public Node tail = null;

	public static class Node {
		int data;
		Node next;
		
		public Node(int value) {
			this.data  = value;
			this.next = null;
		}
	}
	
	public void newNode(int value) {
		Node node = new Node(value);
		
		if (head != null) {
			tail.next = node;
			tail = node;
			
		} else {
			head = node;
			tail = node;
		}
	}
	
	public void printList() {
		Node current = head;
			
		while (current != null) {
			System.out.print(current.data + "  ");
			current = current.next;
		}
	}
	
	public void printReverse(Node hd) {
		if (hd != null) {
			printReverse(hd.next);
			
			System.out.print(hd.data + "  ");
		}
	}
	
	public static void main(String[] args) {
		LinkedListII list = new LinkedListII();
	    list.newNode(1);
	    list.newNode(2);
	    list.newNode(3);
	    list.newNode(4);
	    list.newNode(5);
	    list.newNode(6);
	    list.newNode(7);
	    list.newNode(8);
	    list.newNode(9);
	    list.printList();
	    System.out.println();
	    list.printReverse(list.head);
	}
}