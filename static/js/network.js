class NetworkManager {
    constructor(wsUrl) {
        this.ws = new WebSocket(wsUrl);
        this.nodes = new Map();
        this.links = new Map();
        this.callbacks = {
            onNetworkUpdate: [],
            onNewBlock: []
        };
        
        this.setupWebSocket();
    }
    
    setupWebSocket() {
        this.ws.onmessage = (event) => {
            const message = JSON.parse(event.data);
            
            if (message.type === "network_update") {
                this.callbacks.onNetworkUpdate.forEach(cb => cb(message.data));
            }
            else if (message.type === "new_block") {
                this.handleNewBlock(message.data);
                this.callbacks.onNewBlock.forEach(cb => cb(message.data));
            }
        };
    }
    
    handleNewBlock(block) {
        if (!this.nodes.has(block.sender_id)) {
            this.nodes.set(block.sender_id, {
                id: block.sender_id,
                type: block.node_type
            });
        }
        
        if (!this.nodes.has(block.receiver_id)) {
            this.nodes.set(block.receiver_id, {
                id: block.receiver_id,
                type: "client"
            });
        }
        
        const linkId = `${block.sender_id}-${block.receiver_id}`;
        if (!this.links.has(linkId)) {
            this.links.set(linkId, {
                source: block.sender_id,
                target: block.receiver_id,
                value: block.data_size
            });
        } else {
            this.links.get(linkId).value += block.data_size;
        }
    }
    
    onNetworkUpdate(callback) {
        this.callbacks.onNetworkUpdate.push(callback);
    }
    
    onNewBlock(callback) {
        this.callbacks.onNewBlock.push(callback);
    }
}