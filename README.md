# DVPN Network Visualization System

A decentralized VPN network visualization system that provides real-time monitoring and analysis of network nodes, traffic, and performance metrics.

## Features

- Real-time network visualization
- Provider and client node management
- Secure communication with encryption
- Performance monitoring and metrics
- Interactive dashboard
- Block creation and tracking
- WebSocket-based live updates

## Requirements

- Python 3.9+
- SQLite3
- Node.js 14+ (for frontend development)
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dvpn-network.git
cd dvpn-network
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Copy and configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Running the Application

### Development Mode

1. Start the server:
```bash
python scripts/run_server.py
```

2. Access the dashboard at `http://localhost:8000`

### Production Mode

Using Docker Compose:
```bash
docker-compose up -d
```

Using systemd:
```bash
sudo cp dvpn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable dvpn
sudo systemctl start dvpn
```

## Project Structure

```
dvpn_network/
├── config/           # Configuration files
├── dvpn/            # Main package
│   ├── core/        # Core functionality
│   ├── network/     # Network management
│   ├── api/         # API endpoints
│   └── utils/       # Utility functions
├── static/          # Frontend assets
├── tests/           # Test suite
└── scripts/         # Management scripts
```

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

This project follows PEP 8 guidelines. Use flake8 for linting:
```bash
flake8 dvpn/
```

## Monitoring

The application exports metrics for Prometheus at `/metrics`. Grafana dashboards are available at port 3000.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Security

For security issues, please email security@yourdomain.com instead of using the issue tracker.

## Support

- Documentation: /docs
- Issues: GitHub issue tracker
- Community: Discord server

## Acknowledgments

- D3.js for visualization
- FastAPI framework
- All contributors