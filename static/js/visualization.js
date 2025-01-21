class NetworkVisualization {
    constructor(containerId, width = 800, height = 600) {
        this.width = width;
        this.height = height;
        
        this.svg = d3.select(containerId)
            .append("svg")
            .attr("width", width)
            .attr("height", height);
            
        this.simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id))
            .force("charge", d3.forceManyBody().strength(-300))
            .force("center", d3.forceCenter(width / 2, height / 2));
            
        this.g = this.svg.append("g");
        
        this.setupSimulation();
    }
    
    setupSimulation() {
        this.simulation.on("tick", () => {
            this.g.selectAll(".link")
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);
                
            this.g.selectAll(".node")
                .attr("cx", d => d.x)
                .attr("cy", d => d.y);
        });
    }
    
    updateData(nodes, links) {
        const nodeArray = Array.from(nodes.values());
        const linkArray = Array.from(links.values());
        
        this.updateLinks(linkArray);
        this.updateNodes(nodeArray);
        
        this.simulation
            .nodes(nodeArray)
            .force("link").links(linkArray);
            
        this.simulation.alpha(1).restart();
    }
    
    updateLinks(links) {
        const link = this.g.selectAll(".link")
            .data(links, d => `${d.source}-${d.target}`);
            
        link.enter()
            .append("line")
            .attr("class", "link")
            .merge(link);
            
        link.exit().remove();
    }
    
    updateNodes(nodes) {
        const node = this.g.selectAll(".node")
            .data(nodes, d => d.id);
            
        const nodeEnter = node.enter()
            .append("circle")
            .attr("class", d => `node ${d.type}`)
            .attr("r", 8)
            .call(d3.drag()
                .on("start", this.dragstarted.bind(this))
                .on("drag", this.dragged.bind(this))
                .on("end", this.dragended.bind(this)));
                
        node.exit().remove();
    }
    
    dragstarted(event) {
        if (!event.active) this.simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }
    
    dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }
    
    dragended(event) {
        if (!event.active) this.simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }
}