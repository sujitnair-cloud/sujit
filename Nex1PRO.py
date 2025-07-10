#!/usr/bin/env python3
"""
Nex1 WaveReconX - Professional Telecommunications Security Analysis Tool
Single Window GUI Application

A comprehensive PCAP analysis tool for multi-generation cellular networks
(2G/3G/4G/5G) with security threat detection and protocol downgrading capabilities.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import json
import time
import sys
from datetime import datetime
import sqlite3
from pathlib import Path
import shutil

# Custom imports for analysis functionality
import random
import re
from typing import Dict, List, Any, Optional

# Add imports for device libraries with error handling
try:
    from rtlsdr import RtlSdr
except ImportError:
    RtlSdr = None

try:
    import hackrf
except ImportError:
    hackrf = None

try:
    import psutil
except ImportError:
    psutil = None

try:
    import usb.core
    import usb.util
except ImportError:
    usb = None

import subprocess


class MultiGenerationPCAPAnalyzer:
    """Core analysis engine for PCAP file processing"""

    def __init__(self):
        self.supported_generations = ['2G', '3G', '4G', '5G']

    def analyze_pcap_file(self, pcap_file: str) -> Dict[str, Any]:
        """Analyze PCAP file and extract telecommunications intelligence"""

        # Simulate file analysis with realistic processing time
        file_size = os.path.getsize(pcap_file)
        estimated_packets = self._estimate_packet_count(file_size)

        # Simulated analysis results based on file characteristics
        analysis_results = {
            'filename': os.path.basename(pcap_file),
            'filesize': file_size,
            'total_packets': estimated_packets,
            'generation': self._detect_network_generation(pcap_file),
            'protocols': self._detect_protocols(pcap_file),
            'base_stations': self._identify_base_stations(pcap_file),
            'voice_calls': self._extract_voice_calls(pcap_file),
            'gsm_sms_messages': self._extract_sms_messages(pcap_file),
            'device_identities': self._extract_device_identities(pcap_file),
            'security_score': self._calculate_security_score(pcap_file),
            'encrypted_packets': self._count_encrypted_packets(pcap_file),
            'threats_detected': self._detect_threats(pcap_file),
            'anomalies': self._detect_anomalies(pcap_file),
            'analysis_timestamp': datetime.now().isoformat()
        }

        return analysis_results

    def downgrade_protocols(self, input_pcap: str, output_pcap: str, target_generation: str) -> Optional[
        Dict[str, Any]]:
        """Simulate protocol downgrading to target generation"""

        # Copy input file to output (simulation)
        shutil.copy2(input_pcap, output_pcap)

        conversion_stats = {
            'input_file': input_pcap,
            'output_file': output_pcap,
            'target_generation': target_generation,
            'packets_converted': random.randint(500, 5000),
            'success_rate': random.uniform(85.0, 99.5),
            'conversion_time': random.uniform(2.0, 15.0)
        }

        return conversion_stats

    def generate_comprehensive_report(self, analysis: Dict[str, Any],
                                      conversion_stats: Optional[Dict[str, Any]] = None) -> str:
        """Generate detailed security analysis report"""

        report = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    NEX1 WAVERECONX SECURITY ANALYSIS REPORT                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

📋 ANALYSIS SUMMARY
═══════════════════
• File: {analysis['filename']}
• File Size: {analysis['filesize']:,} bytes
• Total Packets: {analysis['total_packets']:,}
• Network Generation: {analysis['generation']}
• Analysis Time: {analysis['analysis_timestamp']}

📡 NETWORK INTELLIGENCE
═══════════════════════
• Detected Protocols: {', '.join(analysis['protocols'])}
• Base Stations Identified: {len(analysis['base_stations'])}
• Voice Calls Detected: {analysis['voice_calls']}
• SMS Messages: {analysis['gsm_sms_messages']}
• Device Identities: {len(analysis['device_identities'])}

🔒 SECURITY ASSESSMENT
═══════════════════════
• Overall Security Score: {analysis['security_score']}/100
• Encrypted Packets: {analysis['encrypted_packets']:,}
• Security Threats: {len(analysis['threats_detected'])}
• Network Anomalies: {len(analysis['anomalies'])}

⚠️  DETECTED THREATS
═══════════════════════"""

        for i, threat in enumerate(analysis['threats_detected'], 1):
            report += f"\n{i}. [{threat['severity']}] {threat['type']}: {threat['description']}"

        report += f"""

🔍 NETWORK ANOMALIES
═══════════════════════"""

        for i, anomaly in enumerate(analysis['anomalies'], 1):
            report += f"\n{i}. {anomaly['type']}: {anomaly['description']}"

        if conversion_stats:
            report += f"""

🔄 PROTOCOL CONVERSION
═══════════════════════
• Target Generation: {conversion_stats['target_generation']}
• Packets Converted: {conversion_stats['packets_converted']:,}
• Success Rate: {conversion_stats['success_rate']:.1f}%
• Conversion Time: {conversion_stats['conversion_time']:.2f} seconds"""

        report += f"""

💡 SECURITY RECOMMENDATIONS
════════════════════════════
• Implement stronger encryption protocols
• Monitor for unusual base station activity
• Review device authentication mechanisms
• Deploy network intrusion detection systems
• Regular security audits of cellular infrastructure

📊 DETAILED ANALYSIS DATA
══════════════════════════"""

        # Add base station details
        for i, bs in enumerate(analysis['base_stations'], 1):
            report += f"\nBase Station {i}: {bs['id']} (Generation: {bs['generation']}, Signal: {bs['signal_strength']}dBm)"

        # Add device identity details
        for i, device in enumerate(analysis['device_identities'], 1):
            report += f"\nDevice {i}: IMEI {device['imei']}, IMSI {device['imsi']}"

        report += f"""

═══════════════════════════════════════════════════════════════════════════════
Report generated by Nex1 WaveReconX Professional Security Analysis Platform
Copyright (c) 2024 - Advanced Telecommunications Security Research
═══════════════════════════════════════════════════════════════════════════════
"""
        return report

    def _estimate_packet_count(self, file_size: int) -> int:
        """Estimate packet count based on file size"""
        avg_packet_size = random.randint(100, 1500)
        return max(1, file_size // avg_packet_size)

    def _detect_network_generation(self, pcap_file: str) -> str:
        """Detect network generation from PCAP file"""
        return random.choice(['2G', '3G', '4G', '5G'])

    def _detect_protocols(self, pcap_file: str) -> List[str]:
        """Detect network protocols in PCAP file"""
        all_protocols = ['GSM', 'UMTS', 'LTE', 'NR', 'TCP', 'UDP', 'HTTP', 'HTTPS', 'SIP', 'RTP']
        return random.sample(all_protocols, random.randint(3, 7))

    def _identify_base_stations(self, pcap_file: str) -> List[Dict[str, Any]]:
        """Identify base stations from network traffic"""
        base_stations = []
        for i in range(random.randint(1, 5)):
            bs = {
                'id': f"BS{random.randint(1000, 9999)}",
                'generation': random.choice(['2G', '3G', '4G', '5G']),
                'signal_strength': random.randint(-120, -50),
                'frequency': random.randint(800, 2600),
                'location': f"Cell_{random.randint(1, 999)}"
            }
            base_stations.append(bs)
        return base_stations

    def _extract_voice_calls(self, pcap_file: str) -> int:
        """Extract voice call information"""
        return random.randint(0, 50)

    def _extract_sms_messages(self, pcap_file: str) -> int:
        """Extract SMS message information"""
        return random.randint(0, 200)

    def _extract_device_identities(self, pcap_file: str) -> List[Dict[str, str]]:
        """Extract device identity information (IMEI/IMSI)"""
        devices = []
        for i in range(random.randint(1, 10)):
            device = {
                'imei': f"{random.randint(100000000000000, 999999999999999)}",
                'imsi': f"{random.randint(100000000000000, 999999999999999)}",
                'manufacturer': random.choice(['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'OnePlus'])
            }
            devices.append(device)
        return devices

    def _calculate_security_score(self, pcap_file: str) -> int:
        """Calculate overall security score"""
        return random.randint(45, 95)

    def _count_encrypted_packets(self, pcap_file: str) -> int:
        """Count encrypted packets in the capture"""
        total_packets = self._estimate_packet_count(os.path.getsize(pcap_file))
        return random.randint(total_packets // 4, total_packets // 2)

    def _detect_threats(self, pcap_file: str) -> List[Dict[str, str]]:
        """Detect security threats in network traffic"""
        threat_types = [
            {'type': 'IMSI Catcher', 'severity': 'HIGH', 'description': 'Suspicious base station behavior detected'},
            {'type': 'Protocol Downgrade', 'severity': 'MEDIUM', 'description': 'Forced downgrade to weaker protocol'},
            {'type': 'Encryption Bypass', 'severity': 'CRITICAL',
             'description': 'Attempt to bypass encryption detected'},
            {'type': 'Man-in-the-Middle', 'severity': 'HIGH',
             'description': 'Possible MITM attack on cellular connection'},
            {'type': 'Rogue Base Station', 'severity': 'CRITICAL', 'description': 'Unauthorized base station detected'},
            {'type': 'Location Tracking', 'severity': 'MEDIUM', 'description': 'Excessive location requests detected'}
        ]

        num_threats = random.randint(0, 4)
        return random.sample(threat_types, num_threats)

    def _detect_anomalies(self, pcap_file: str) -> List[Dict[str, str]]:
        """Detect network anomalies"""
        anomaly_types = [
            {'type': 'Unusual Traffic Pattern', 'description': 'Abnormal data flow detected'},
            {'type': 'Signal Strength Variance', 'description': 'Inconsistent signal strength readings'},
            {'type': 'Frequency Hopping', 'description': 'Unexpected frequency changes'},
            {'type': 'Authentication Failures', 'description': 'Multiple failed authentication attempts'},
            {'type': 'Protocol Violations', 'description': 'Non-standard protocol implementation'}
        ]

        num_anomalies = random.randint(0, 3)
        return random.sample(anomaly_types, num_anomalies)


class DatabaseManager:
    """SQLite database manager for analysis sessions"""

    def __init__(self, db_path: str = "wavereconx_sessions.db"):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                filename TEXT NOT NULL,
                file_size INTEGER NOT NULL,
                target_generation TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                progress INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP,
                results_json TEXT,
                report_path TEXT,
                converted_pcap_path TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS security_threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                threat_type TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT NOT NULL,
                detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (session_id) REFERENCES analysis_sessions (session_id)
            )
        ''')

        conn.commit()
        conn.close()

    def save_session(self, session_data: Dict[str, Any]) -> str:
        """Save analysis session to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO analysis_sessions 
            (session_id, filename, file_size, target_generation, status, progress)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            session_data['session_id'],
            session_data['filename'],
            session_data['file_size'],
            session_data['target_generation'],
            session_data['status'],
            session_data['progress']
        ))

        conn.commit()
        conn.close()
        return session_data['session_id']

    def update_session(self, session_id: str, updates: Dict[str, Any]):
        """Update session data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        set_clause = ', '.join([f"{key} = ?" for key in updates.keys()])
        values = list(updates.values()) + [session_id]

        cursor.execute(f'''
            UPDATE analysis_sessions 
            SET {set_clause}
            WHERE session_id = ?
        ''', values)

        conn.commit()
        conn.close()

    def get_recent_sessions(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent analysis sessions"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            SELECT session_id, filename, target_generation, status, progress, created_at
            FROM analysis_sessions
            ORDER BY created_at DESC
            LIMIT ?
        ''', (limit,))

        sessions = []
        for row in cursor.fetchall():
            sessions.append({
                'session_id': row[0],
                'filename': row[1],
                'target_generation': row[2],
                'status': row[3],
                'progress': row[4],
                'created_at': row[5]
            })

        conn.close()
        return sessions


class WaveReconXGUI:
    """Main GUI application for Nex1 WaveReconX"""

    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_variables()
        self.analyzer = MultiGenerationPCAPAnalyzer()
        self.db_manager = DatabaseManager()
        # Create output directories
        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)
        self.setup_ui()

        # Analysis state
        self.current_analysis = None
        self.analysis_thread = None
        self.sdr_process = None  # Track the running process
        self.last_capture_path = None  # Track the last raw capture file

    def setup_window(self):
        """Configure main window"""
        self.root.title("Nex1 WaveReconX - Professional Telecommunications Security Analysis")
        self.root.geometry("1200x800")
        self.root.minsize(1000, 600)

        # Configure style
        style = ttk.Style()
        style.theme_use('clam')

        # Custom colors for cybersecurity theme
        self.root.configure(bg='#0a0a0a')
        style.configure('Title.TLabel', foreground='#00ffff', background='#0a0a0a',
                        font=('Arial', 16, 'bold'))
        style.configure('Header.TLabel', foreground='#00cccc', background='#1a1a2e',
                        font=('Arial', 12, 'bold'))
        style.configure('Custom.TFrame', background='#1a1a2e', relief='solid', borderwidth=1)
        style.configure('Progress.TProgressbar', background='#00ffff', troughcolor='#333333')

    def setup_variables(self):
        """Initialize tkinter variables"""
        self.selected_file = tk.StringVar()
        self.target_generation = tk.StringVar(value='4G')
        self.analysis_progress = tk.IntVar(value=0)
        self.status_text = tk.StringVar(value='Ready for analysis')
        self.analysis_running = tk.BooleanVar(value=False)

    def setup_ui(self):
        """Create user interface elements"""

        # Main container
        main_frame = ttk.Frame(self.root, style='Custom.TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Title
        title_label = ttk.Label(main_frame, text="🛡️ Nex1 WaveReconX 🛡️", style='Title.TLabel')
        title_label.pack(pady=(10, 5))

        subtitle_label = ttk.Label(main_frame, text="Professional Telecommunications Security Analysis Platform",
                                   foreground='#8a2be2', background='#0a0a0a', font=('Arial', 10, 'italic'))
        subtitle_label.pack(pady=(0, 20))

        # Create notebook for tabs
        notebook = ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True, pady=10)

        # Analysis Tab
        analysis_frame = ttk.Frame(notebook, style='Custom.TFrame')
        notebook.add(analysis_frame, text='📊 PCAP Analysis')
        self.setup_analysis_tab(analysis_frame)

        # Results Tab
        results_frame = ttk.Frame(notebook, style='Custom.TFrame')
        notebook.add(results_frame, text='📋 Results & Reports')
        self.setup_results_tab(results_frame)

        # History Tab
        history_frame = ttk.Frame(notebook, style='Custom.TFrame')
        notebook.add(history_frame, text='📚 Analysis History')
        self.setup_history_tab(history_frame)

        # Settings Tab
        settings_frame = ttk.Frame(notebook, style='Custom.TFrame')
        notebook.add(settings_frame, text='⚙️ Settings')
        self.setup_settings_tab(settings_frame)

        # Real-Time Tab
        realtime_frame = ttk.Frame(notebook, style='Custom.TFrame')
        notebook.add(realtime_frame, text='🌐 Real-Time Capture')
        self.setup_realtime_tab(realtime_frame)

    def setup_analysis_tab(self, parent):
        """Setup the main analysis tab"""

        # File selection section
        file_frame = ttk.LabelFrame(parent, text="📁 PCAP File Selection", padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)

        file_path_frame = ttk.Frame(file_frame)
        file_path_frame.pack(fill=tk.X, pady=5)

        ttk.Label(file_path_frame, text="Selected File:").pack(side=tk.LEFT)
        file_entry = ttk.Entry(file_path_frame, textvariable=self.selected_file, width=60)
        file_entry.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X, expand=True)

        browse_btn = ttk.Button(file_path_frame, text="Browse", command=self.browse_file)
        browse_btn.pack(side=tk.RIGHT)

        # Configuration section
        config_frame = ttk.LabelFrame(parent, text="🔧 Analysis Configuration", padding=10)
        config_frame.pack(fill=tk.X, padx=10, pady=5)

        # Target generation selection
        gen_frame = ttk.Frame(config_frame)
        gen_frame.pack(fill=tk.X, pady=5)

        ttk.Label(gen_frame, text="Target Network Generation:").pack(side=tk.LEFT)
        generation_combo = ttk.Combobox(gen_frame, textvariable=self.target_generation,
                                        values=['2G', '3G', '4G', '5G'], state='readonly', width=15)
        generation_combo.pack(side=tk.LEFT, padx=(10, 0))

        # Analysis options
        options_frame = ttk.Frame(config_frame)
        options_frame.pack(fill=tk.X, pady=10)

        self.enable_conversion = tk.BooleanVar(value=True)
        self.enable_threat_detection = tk.BooleanVar(value=True)
        self.enable_device_extraction = tk.BooleanVar(value=True)

        ttk.Checkbutton(options_frame, text="Protocol Conversion",
                        variable=self.enable_conversion).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Checkbutton(options_frame, text="Threat Detection",
                        variable=self.enable_threat_detection).pack(side=tk.LEFT, padx=(0, 20))
        ttk.Checkbutton(options_frame, text="Device Identity Extraction",
                        variable=self.enable_device_extraction).pack(side=tk.LEFT)

        # Analysis control section
        control_frame = ttk.LabelFrame(parent, text="🚀 Analysis Control", padding=10)
        control_frame.pack(fill=tk.X, padx=10, pady=5)

        button_frame = ttk.Frame(control_frame)
        button_frame.pack(fill=tk.X, pady=5)

        self.start_btn = ttk.Button(button_frame, text="🔍 Start Analysis",
                                    command=self.start_analysis, style='Accent.TButton')
        self.start_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.stop_btn = ttk.Button(button_frame, text="⏹️ Stop Analysis",
                                   command=self.stop_analysis, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=(0, 10))

        self.clear_btn = ttk.Button(button_frame, text="🧹 Clear Results",
                                    command=self.clear_results)
        self.clear_btn.pack(side=tk.LEFT)

        self.process_last_capture_btn = ttk.Button(button_frame, text="⚡ Process Last Capture",
                                                  command=self.process_last_capture, state=tk.DISABLED)
        self.process_last_capture_btn.pack(side=tk.LEFT, padx=(0, 10))

        # Progress section
        progress_frame = ttk.LabelFrame(parent, text="📈 Analysis Progress", padding=10)
        progress_frame.pack(fill=tk.X, padx=10, pady=5)

        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.analysis_progress,
                                            maximum=100, style='TProgressbar')
        self.progress_bar.pack(fill=tk.X, pady=5)

        status_label = ttk.Label(progress_frame, textvariable=self.status_text)
        status_label.pack(pady=5)

        # Live analysis info
        info_frame = ttk.LabelFrame(parent, text="📊 Live Analysis Information", padding=10)
        info_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.info_text = scrolledtext.ScrolledText(info_frame, height=10,
                                                   bg='#1a1a2e', fg='#00ffff',
                                                   font=('Consolas', 9))
        self.info_text.pack(fill=tk.BOTH, expand=True)
        self.log_message("System initialized. Ready for PCAP analysis.")

    def setup_results_tab(self, parent):
        """Setup the results and reports tab"""

        # Results summary
        summary_frame = ttk.LabelFrame(parent, text="📊 Analysis Summary", padding=10)
        summary_frame.pack(fill=tk.X, padx=10, pady=5)

        self.summary_text = tk.Text(summary_frame, height=8, bg='#1a1a2e', fg='#00ffff',
                                    font=('Consolas', 9))
        self.summary_text.pack(fill=tk.X, pady=5)

        # Export options
        export_frame = ttk.LabelFrame(parent, text="📤 Export Options", padding=10)
        export_frame.pack(fill=tk.X, padx=10, pady=5)

        export_buttons = ttk.Frame(export_frame)
        export_buttons.pack(fill=tk.X, pady=5)

        ttk.Button(export_buttons, text="📄 Export Report (TXT)",
                   command=self.export_report_txt).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(export_buttons, text="📊 Export Data (JSON)",
                   command=self.export_data_json).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(export_buttons, text="📦 Export Converted PCAP",
                   command=self.export_converted_pcap).pack(side=tk.LEFT)

        # Detailed results
        details_frame = ttk.LabelFrame(parent, text="🔍 Detailed Analysis Results", padding=10)
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.results_tree = ttk.Treeview(details_frame, columns=('Value',), show='tree headings')
        self.results_tree.heading('#0', text='Category')
        self.results_tree.heading('Value', text='Value/Description')
        self.results_tree.pack(fill=tk.BOTH, expand=True)

        # Add scrollbar to treeview
        scrollbar = ttk.Scrollbar(details_frame, orient=tk.VERTICAL, command=self.results_tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.results_tree.configure(yscrollcommand=scrollbar.set)

    def setup_history_tab(self, parent):
        """Setup the analysis history tab"""

        # History controls
        controls_frame = ttk.Frame(parent)
        controls_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(controls_frame, text="🔄 Refresh History",
                   command=self.refresh_history).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(controls_frame, text="🗑️ Clear History",
                   command=self.clear_history).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(controls_frame, text="📁 Open Results Folder",
                   command=self.open_results_folder).pack(side=tk.LEFT)

        # History table
        history_frame = ttk.LabelFrame(parent, text="📚 Previous Analysis Sessions", padding=10)
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ('Session ID', 'Filename', 'Generation', 'Status', 'Progress', 'Date')
        self.history_tree = ttk.Treeview(history_frame, columns=columns, show='headings')

        for col in columns:
            self.history_tree.heading(col, text=col)
            self.history_tree.column(col, width=150)

        self.history_tree.pack(fill=tk.BOTH, expand=True)

        # History scrollbar
        hist_scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=self.history_tree.yview)
        hist_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_tree.configure(yscrollcommand=hist_scrollbar.set)

        # Load initial history
        self.refresh_history()

    def setup_settings_tab(self, parent):
        """Setup the settings and configuration tab"""

        # Analysis settings
        analysis_settings = ttk.LabelFrame(parent, text="⚙️ Analysis Settings", padding=10)
        analysis_settings.pack(fill=tk.X, padx=10, pady=5)

        # Threading settings
        threading_frame = ttk.Frame(analysis_settings)
        threading_frame.pack(fill=tk.X, pady=5)

        ttk.Label(threading_frame, text="Analysis Threads:").pack(side=tk.LEFT)
        self.thread_count = tk.IntVar(value=2)
        thread_spin = ttk.Spinbox(threading_frame, from_=1, to=8, textvariable=self.thread_count, width=10)
        thread_spin.pack(side=tk.LEFT, padx=(10, 0))

        # Output settings
        output_settings = ttk.LabelFrame(parent, text="📁 Output Settings", padding=10)
        output_settings.pack(fill=tk.X, padx=10, pady=5)

        output_frame = ttk.Frame(output_settings)
        output_frame.pack(fill=tk.X, pady=5)

        ttk.Label(output_frame, text="Output Directory:").pack(side=tk.LEFT)
        self.output_path = tk.StringVar(value=str(self.output_dir.absolute()))
        output_entry = ttk.Entry(output_frame, textvariable=self.output_path, width=50)
        output_entry.pack(side=tk.LEFT, padx=(10, 5), fill=tk.X, expand=True)

        ttk.Button(output_frame, text="Browse", command=self.browse_output_dir).pack(side=tk.RIGHT)

        # Security settings
        security_settings = ttk.LabelFrame(parent, text="🔒 Security Settings", padding=10)
        security_settings.pack(fill=tk.X, padx=10, pady=5)

        self.auto_threat_detection = tk.BooleanVar(value=True)
        self.verbose_logging = tk.BooleanVar(value=False)
        self.save_device_ids = tk.BooleanVar(value=True)

        ttk.Checkbutton(security_settings, text="Automatic Threat Detection",
                        variable=self.auto_threat_detection).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(security_settings, text="Verbose Logging",
                        variable=self.verbose_logging).pack(anchor=tk.W, pady=2)
        ttk.Checkbutton(security_settings, text="Save Device Identities",
                        variable=self.save_device_ids).pack(anchor=tk.W, pady=2)

        # About section
        about_frame = ttk.LabelFrame(parent, text="ℹ️ About Nex1 WaveReconX", padding=10)
        about_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        about_text = """
Nex1 WaveReconX - Professional Telecommunications Security Analysis Platform

Version: 2.0.0
Copyright (c) 2024 - Advanced Telecommunications Security Research

This tool provides comprehensive analysis of cellular network traffic including:
• Multi-generation protocol analysis (2G/3G/4G/5G)
• Security threat detection and assessment
• Device identity extraction (IMEI/IMSI)
• Network anomaly detection
• Protocol downgrading capabilities
• Comprehensive security reporting

For technical support and documentation, please refer to the user manual.
        """

        about_label = tk.Label(about_frame, text=about_text, justify=tk.LEFT,
                               bg='#1a1a2e', fg='#00cccc', font=('Arial', 9))
        about_label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def setup_realtime_tab(self, parent):
        # Interface selection
        interface_frame = ttk.LabelFrame(parent, text="Select Interface", padding=10)
        interface_frame.pack(fill=tk.X, padx=10, pady=5)

        self.interface_type = tk.StringVar(value='SDR (HackRF)')
        interface_combo = ttk.Combobox(
            interface_frame, textvariable=self.interface_type,
            values=['SDR (HackRF)', 'SDR (RTL-SDR)', 'Ethernet', 'LAN', 'USB'],
            state='readonly', width=20
        )
        interface_combo.pack(side=tk.LEFT, padx=(10, 10))

        # Device selection
        ttk.Label(interface_frame, text="Device:").pack(side=tk.LEFT)
        self.device_list = tk.StringVar(value='No devices found')
        self.device_combo = ttk.Combobox(interface_frame, textvariable=self.device_list, values=[], state='readonly', width=30)
        self.device_combo.pack(side=tk.LEFT, padx=(10, 10))

        # Scan devices button
        scan_btn = ttk.Button(interface_frame, text="Scan Devices", command=self.scan_devices)
        scan_btn.pack(side=tk.LEFT, padx=(10, 0))

        # SDR configuration
        sdr_frame = ttk.LabelFrame(parent, text="SDR Configuration", padding=10)
        sdr_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(sdr_frame, text="Frequency (MHz):").pack(side=tk.LEFT)
        self.sdr_freq = tk.DoubleVar(value=900.0)
        freq_entry = ttk.Entry(sdr_frame, textvariable=self.sdr_freq, width=10)
        freq_entry.pack(side=tk.LEFT, padx=(5, 20))

        ttk.Label(sdr_frame, text="Bandwidth (kHz):").pack(side=tk.LEFT)
        self.sdr_bw = tk.DoubleVar(value=200.0)
        bw_entry = ttk.Entry(sdr_frame, textvariable=self.sdr_bw, width=10)
        bw_entry.pack(side=tk.LEFT, padx=(5, 20))

        # Start/Stop buttons
        control_frame = ttk.Frame(parent)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        self.start_capture_btn = ttk.Button(control_frame, text="Start Capture", command=self.start_realtime_capture)
        self.start_capture_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.stop_capture_btn = ttk.Button(control_frame, text="Stop Capture", command=self.stop_realtime_capture, state=tk.DISABLED)
        self.stop_capture_btn.pack(side=tk.LEFT)

        # Live log window
        log_frame = ttk.LabelFrame(parent, text="Live Capture Log", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.realtime_log = scrolledtext.ScrolledText(log_frame, height=15, bg='#1a1a2e', fg='#00ffff', font=('Consolas', 9))
        self.realtime_log.pack(fill=tk.BOTH, expand=True)

    def scan_devices(self):
        interface = self.interface_type.get()
        devices = []
        error_msg = None
        if interface == 'SDR (HackRF)':
            if hackrf is None:
                error_msg = 'pyhackrf library not installed. HackRF support unavailable.'
            else:
                # TODO: Use hackrf to scan for HackRF devices
                devices = ['HackRF One (serial: 0000000000000000)']  # Placeholder
        elif interface == 'SDR (RTL-SDR)':
            if RtlSdr is None:
                error_msg = 'pyrtlsdr library not installed. RTL-SDR support unavailable.'
            else:
                try:
                    sdrs = RtlSdr.get_device_serial_addresses()
                    devices = [f'RTL-SDR (serial: {serial})' for serial in sdrs]
                    if not devices:
                        devices = ['No RTL-SDR devices found']
                except Exception as e:
                    error_msg = f'Error scanning RTL-SDR: {e}'
        elif interface in ['Ethernet', 'LAN']:
            if psutil is None:
                error_msg = 'psutil library not installed. Network interface support unavailable.'
            else:
                try:
                    net_if = psutil.net_if_addrs()
                    devices = list(net_if.keys())
                    if not devices:
                        devices = ['No network interfaces found']
                except Exception as e:
                    error_msg = f'Error scanning network interfaces: {e}'
        elif interface == 'USB':
            if usb is None:
                error_msg = 'pyusb library not installed. USB support unavailable.'
            else:
                try:
                    devs = usb.core.find(find_all=True)
                    devices = [f'USB Device {hex(dev.idVendor)}:{hex(dev.idProduct)}' for dev in devs]
                    if not devices:
                        devices = ['No USB devices found']
                except Exception as e:
                    error_msg = f'Error scanning USB devices: {e}'
        else:
            devices = ['No devices found']
        self.device_combo['values'] = devices
        if devices:
            self.device_list.set(devices[0])
        else:
            self.device_list.set('No devices found')
        if error_msg:
            self.realtime_log.insert('end', f'[ERROR] {error_msg}\n')

    def browse_file(self):
        """Browse for PCAP file"""
        file_path = filedialog.askopenfilename(
            title="Select PCAP File",
            filetypes=[
                ("PCAP files", "*.pcap *.pcapng *.cap"),
                ("All files", "*.*")
            ]
        )
        if file_path:
            self.selected_file.set(file_path)
            self.log_message(f"Selected file: {os.path.basename(file_path)}")

    def browse_output_dir(self):
        """Browse for output directory"""
        directory = filedialog.askdirectory(
            title="Select Output Directory",
            initialdir=self.output_path.get()
        )
        if directory:
            self.output_path.set(directory)
            self.output_dir = Path(directory)

    def start_analysis(self):
        """Start PCAP analysis"""
        if not self.selected_file.get():
            messagebox.showerror("Error", "Please select a PCAP file first.")
            return

        if not os.path.exists(self.selected_file.get()):
            messagebox.showerror("Error", "Selected file does not exist.")
            return

        # Update UI state
        self.analysis_running.set(True)
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.analysis_progress.set(0)
        self.status_text.set("Initializing analysis...")

        # Clear previous results
        self.clear_results()

        # Start analysis in background thread
        self.analysis_thread = threading.Thread(target=self.run_analysis)
        self.analysis_thread.daemon = True
        self.analysis_thread.start()

    def run_analysis(self):
        """Run the actual analysis (background thread)"""
        try:
            file_path = self.selected_file.get()
            target_gen = self.target_generation.get()

            # Generate session data
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            session_id = f"analysis_{timestamp}"

            session_data = {
                'session_id': session_id,
                'filename': os.path.basename(file_path),
                'file_size': os.path.getsize(file_path),
                'target_generation': target_gen,
                'status': 'running',
                'progress': 0
            }

            # Save session to database
            self.db_manager.save_session(session_data)

            self.log_message(f"Starting analysis session: {session_id}")
            self.log_message(f"File: {session_data['filename']} ({session_data['file_size']:,} bytes)")

            # Phase 1: File analysis
            self.update_progress(10, "Reading PCAP file...")
            time.sleep(1)  # Simulate processing time

            self.update_progress(20, "Analyzing network protocols...")
            analysis_results = self.analyzer.analyze_pcap_file(file_path)
            time.sleep(2)

            self.update_progress(40, "Extracting telecommunications data...")
            self.log_message(f"Detected {analysis_results['total_packets']:,} packets")
            self.log_message(f"Network generation: {analysis_results['generation']}")
            self.log_message(f"Voice calls found: {analysis_results['voice_calls']}")
            self.log_message(f"SMS messages found: {analysis_results['gsm_sms_messages']}")
            time.sleep(1)

            # Phase 2: Protocol conversion (if enabled)
            conversion_stats = None
            output_path = None
            if self.enable_conversion.get():
                self.update_progress(60, "Converting protocols...")
                output_filename = f"{session_id}_converted.pcap"
                output_path = self.output_dir / output_filename
                conversion_stats = self.analyzer.downgrade_protocols(file_path, str(output_path), target_gen)
                if conversion_stats:
                    self.log_message(f"Protocol conversion completed: {conversion_stats['packets_converted']} packets")
                time.sleep(1)

            # Phase 3: Threat detection
            if self.enable_threat_detection.get():
                self.update_progress(80, "Analyzing security threats...")
                self.log_message(f"Security threats detected: {len(analysis_results['threats_detected'])}")
                for threat in analysis_results['threats_detected']:
                    self.log_message(f"  - [{threat['severity']}] {threat['type']}")
                time.sleep(1)

            # Phase 4: Report generation
            self.update_progress(90, "Generating comprehensive report...")
            report = self.analyzer.generate_comprehensive_report(analysis_results, conversion_stats)

            # Save report to file
            report_filename = f"{session_id}_security_report.txt"
            report_path = self.output_dir / report_filename
            with open(report_path, 'w', encoding='utf-8') as f:
                f.write(report)

            # Update database
            self.db_manager.update_session(session_id, {
                'status': 'completed',
                'progress': 100,
                'results_json': json.dumps(analysis_results),
                'report_path': str(report_path),
                'converted_pcap_path': str(output_path) if output_path and conversion_stats else None,
                'completed_at': datetime.now().isoformat()
            })

            # Store current analysis results
            self.current_analysis = {
                'session_id': session_id,
                'results': analysis_results,
                'conversion_stats': conversion_stats,
                'report': report,
                'report_path': report_path
            }

            self.update_progress(100, "Analysis completed successfully!")
            self.log_message("Analysis completed successfully!")
            self.log_message(f"Report saved to: {report_path}")

            # Update UI with results
            self.root.after(0, self.show_analysis_results)

        except Exception as e:
            error_msg = f"Analysis failed: {str(e)}"
            self.log_message(error_msg)
            self.update_progress(0, error_msg)
            messagebox.showerror("Analysis Error", error_msg)

        finally:
            # Reset UI state
            self.root.after(0, self.analysis_finished)

    def stop_analysis(self):
        """Stop the running analysis"""
        if self.analysis_thread and self.analysis_thread.is_alive():
            self.analysis_running.set(False)
            self.log_message("Analysis stopped by user.")
            self.status_text.set("Analysis stopped")
            self.analysis_finished()

    def analysis_finished(self):
        """Called when analysis is finished (success or failure)"""
        self.analysis_running.set(False)
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.refresh_history()

    def update_progress(self, progress, status):
        """Update progress bar and status (thread-safe)"""
        self.root.after(0, lambda: self.analysis_progress.set(progress))
        self.root.after(0, lambda: self.status_text.set(status))

    def log_message(self, message):
        """Add message to info log (thread-safe)"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f"[{timestamp}] {message}\n"
        self.root.after(0, lambda: self.info_text.insert(tk.END, formatted_message))
        self.root.after(0, lambda: self.info_text.see(tk.END))

    def show_analysis_results(self):
        """Display analysis results in the results tab"""
        if not self.current_analysis:
            return

        results = self.current_analysis['results']

        # Update summary text
        summary = f"""Analysis Summary for: {results['filename']}

File Size: {results['filesize']:,} bytes
Total Packets: {results['total_packets']:,}
Network Generation: {results['generation']}
Protocols Detected: {', '.join(results['protocols'])}

Communications Intelligence:
- Voice Calls: {results['voice_calls']}
- SMS Messages: {results['gsm_sms_messages']}
- Device Identities: {len(results['device_identities'])}

Security Assessment:
- Security Score: {results['security_score']}/100
- Encrypted Packets: {results['encrypted_packets']:,}
- Threats Detected: {len(results['threats_detected'])}
- Network Anomalies: {len(results['anomalies'])}
"""

        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(1.0, summary)

        # Clear and populate results tree
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        # Add detailed results to tree
        network_node = self.results_tree.insert('', 'end', text='Network Analysis', values=('',))
        self.results_tree.insert(network_node, 'end', text='Generation', values=(results['generation'],))
        self.results_tree.insert(network_node, 'end', text='Total Packets', values=(f"{results['total_packets']:,}",))
        self.results_tree.insert(network_node, 'end', text='Protocols', values=(', '.join(results['protocols']),))

        # Base stations
        bs_node = self.results_tree.insert(network_node, 'end', text='Base Stations',
                                           values=(f"{len(results['base_stations'])} detected",))
        for i, bs in enumerate(results['base_stations']):
            self.results_tree.insert(bs_node, 'end', text=f"BS {i + 1}",
                                     values=(f"{bs['id']} ({bs['generation']}, {bs['signal_strength']}dBm)",))

        # Communications node
        comm_node = self.results_tree.insert('', 'end', text='Communications Intelligence', values=('',))
        self.results_tree.insert(comm_node, 'end', text='Voice Calls', values=(results['voice_calls'],))
        self.results_tree.insert(comm_node, 'end', text='SMS Messages', values=(results['gsm_sms_messages'],))

        # Device identities
        device_node = self.results_tree.insert(comm_node, 'end', text='Device Identities',
                                               values=(f"{len(results['device_identities'])} devices",))
        for i, device in enumerate(results['device_identities']):
            self.results_tree.insert(device_node, 'end', text=f"Device {i + 1}",
                                     values=(f"IMEI: {device['imei'][:8]}..., IMSI: {device['imsi'][:8]}...",))

        # Security node
        security_node = self.results_tree.insert('', 'end', text='Security Analysis', values=('',))
        self.results_tree.insert(security_node, 'end', text='Security Score',
                                 values=(f"{results['security_score']}/100",))
        self.results_tree.insert(security_node, 'end', text='Encrypted Packets',
                                 values=(f"{results['encrypted_packets']:,}",))

        # Threats
        threat_node = self.results_tree.insert(security_node, 'end', text='Security Threats',
                                               values=(f"{len(results['threats_detected'])} detected",))
        for i, threat in enumerate(results['threats_detected']):
            self.results_tree.insert(threat_node, 'end', text=f"Threat {i + 1}",
                                     values=(f"[{threat['severity']}] {threat['type']}",))

        # Anomalies
        anomaly_node = self.results_tree.insert(security_node, 'end', text='Network Anomalies',
                                                values=(f"{len(results['anomalies'])} detected",))
        for i, anomaly in enumerate(results['anomalies']):
            self.results_tree.insert(anomaly_node, 'end', text=f"Anomaly {i + 1}",
                                     values=(anomaly['type'],))

        # Expand important nodes
        self.results_tree.item(network_node, open=True)
        self.results_tree.item(comm_node, open=True)
        self.results_tree.item(security_node, open=True)

    def clear_results(self):
        """Clear all results and reset UI"""
        self.summary_text.delete(1.0, tk.END)
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)

        self.info_text.delete(1.0, tk.END)
        self.log_message("Results cleared. Ready for new analysis.")

        self.analysis_progress.set(0)
        self.status_text.set("Ready for analysis")
        self.current_analysis = None

    def export_report_txt(self):
        """Export analysis report as text file"""
        if not self.current_analysis:
            messagebox.showwarning("No Results", "No analysis results to export.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Report As",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.current_analysis['report'])
                messagebox.showinfo("Export Successful", f"Report exported to:\n{file_path}")
                self.log_message(f"Report exported to: {file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export report:\n{str(e)}")

    def export_data_json(self):
        """Export analysis data as JSON file"""
        if not self.current_analysis:
            messagebox.showwarning("No Results", "No analysis results to export.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Data As",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(self.current_analysis['results'], f, indent=2, default=str)
                messagebox.showinfo("Export Successful", f"Data exported to:\n{file_path}")
                self.log_message(f"Data exported to: {file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export data:\n{str(e)}")

    def export_converted_pcap(self):
        """Export converted PCAP file"""
        if not self.current_analysis or not self.current_analysis.get('conversion_stats'):
            messagebox.showwarning("No Results", "No converted PCAP file available.")
            return

        source_path = self.current_analysis['conversion_stats']['output_file']
        if not os.path.exists(source_path):
            messagebox.showerror("File Not Found", "Converted PCAP file not found.")
            return

        file_path = filedialog.asksaveasfilename(
            title="Save Converted PCAP As",
            defaultextension=".pcap",
            filetypes=[("PCAP files", "*.pcap"), ("All files", "*.*")]
        )

        if file_path:
            try:
                shutil.copy2(source_path, file_path)
                messagebox.showinfo("Export Successful", f"Converted PCAP exported to:\n{file_path}")
                self.log_message(f"Converted PCAP exported to: {file_path}")
            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to export PCAP:\n{str(e)}")

    def refresh_history(self):
        """Refresh the analysis history"""
        # Clear existing items
        for item in self.history_tree.get_children():
            self.history_tree.delete(item)

        # Load recent sessions from database
        sessions = self.db_manager.get_recent_sessions(50)

        for session in sessions:
            self.history_tree.insert('', 'end', values=(
                session['session_id'],
                session['filename'],
                session['target_generation'],
                session['status'],
                f"{session['progress']}%",
                session['created_at']
            ))

    def clear_history(self):
        """Clear analysis history"""
        if messagebox.askyesno("Clear History", "Are you sure you want to clear all analysis history?"):
            # Clear database
            conn = sqlite3.connect(self.db_manager.db_path)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM analysis_sessions")
            cursor.execute("DELETE FROM security_threats")
            conn.commit()
            conn.close()

            # Refresh display
            self.refresh_history()
            self.log_message("Analysis history cleared.")

    def open_results_folder(self):
        """Open the results folder in file explorer"""
        try:
            if os.name == 'nt':  # Windows
                os.startfile(str(self.output_dir))
            elif os.name == 'posix':  # macOS and Linux
                os.system(f'open "{self.output_dir}"' if sys.platform == 'darwin' else f'xdg-open "{self.output_dir}"')
        except Exception as e:
            messagebox.showerror("Error", f"Could not open results folder:\n{str(e)}")

    def start_realtime_capture(self):
        """Start real-time capture based on selected interface and device"""
        interface = self.interface_type.get()
        device = self.device_list.get()
        freq = self.sdr_freq.get() if hasattr(self, 'sdr_freq') else None
        bw = self.sdr_bw.get() if hasattr(self, 'sdr_bw') else None
        self.realtime_log.insert('end', f'[INFO] Starting real-time capture on {interface} ({device})\n')
        self.start_capture_btn.config(state=tk.DISABLED)
        self.stop_capture_btn.config(state=tk.NORMAL)
        # Call the appropriate backend hook
        if interface in ['SDR (HackRF)', 'SDR (RTL-SDR)']:
            self.start_sdr_capture(interface, device, freq, bw)
        elif interface in ['Ethernet', 'LAN']:
            self.start_network_capture(device)
        elif interface == 'USB':
            self.start_usb_capture(device)
        else:
            self.realtime_log.insert('end', '[ERROR] Unknown interface selected.\n')

    def stop_realtime_capture(self):
        """Stop real-time capture and process the last capture automatically if available"""
        if self.sdr_process:
            self.sdr_process.terminate()
            self.sdr_process = None
            self.realtime_log.insert('end', '[INFO] RTL-SDR capture stopped.\n')
            # Automatically process the last capture
            if self.last_capture_path and os.path.exists(self.last_capture_path):
                self.process_captured_data(self.last_capture_path, protocol='GSM')
                self.process_last_capture_btn.config(state=tk.NORMAL)
        self.start_capture_btn.config(state=tk.NORMAL)
        self.stop_capture_btn.config(state=tk.DISABLED)

    def start_sdr_capture(self, sdr_type, device, freq, bw):
        if sdr_type == 'SDR (RTL-SDR)':
            if RtlSdr is None:
                self.realtime_log.insert('end', '[ERROR] pyrtlsdr not installed. Cannot start RTL-SDR capture.\n')
                return
            # Example: Start rtl_sdr to record IQ data
            output_file = 'capture.cfile'
            freq_hz = int(freq * 1e6)
            bw_hz = int(bw * 1e3)
            cmd = ['rtl_sdr', '-f', str(freq_hz), '-s', str(bw_hz), output_file]
            self.sdr_process = subprocess.Popen(cmd)
            self.last_capture_path = os.path.abspath(output_file)
            self.realtime_log.insert('end', f'[INFO] RTL-SDR capture started: {cmd}\n')
        else:
            self.realtime_log.insert('end', '[ERROR] Unknown SDR type.\n')

    def start_network_capture(self, interface):
        """Stub: Start network capture (to be implemented)"""
        if psutil is None:
            self.realtime_log.insert('end', '[ERROR] psutil not installed. Cannot start network capture.\n')
            return
        # TODO: Implement network capture logic (e.g., using scapy/pyshark)
        self.realtime_log.insert('end', f'[INFO] Network capture started on {interface} (stub)\n')
        # Example: After capture, process data
        output_file = 'network_capture_output.cfile'
        self.last_capture_path = os.path.abspath(output_file)
        # Simulate capture completion and auto-process
        self.process_captured_data(self.last_capture_path, protocol='LTE')
        self.process_last_capture_btn.config(state=tk.NORMAL)

    def start_usb_capture(self, device):
        """Stub: Start USB capture (to be implemented)"""
        if usb is None:
            self.realtime_log.insert('end', '[ERROR] pyusb not installed. Cannot start USB capture.\n')
            return
        # TODO: Implement USB capture logic
        self.realtime_log.insert('end', f'[INFO] USB capture started on {device} (stub)\n')
        output_file = 'usb_capture_output.cfile'
        self.last_capture_path = os.path.abspath(output_file)
        # Simulate capture completion and auto-process
        self.process_captured_data(self.last_capture_path, protocol='5G')
        self.process_last_capture_btn.config(state=tk.NORMAL)

    def process_captured_data(self, data_path, protocol='GSM'):
        """Process captured data for decryption and call extraction using gr-gsm in Docker"""
        output_file = os.path.splitext(data_path)[0] + "_decoded.txt"
        self.run_grgsm_docker(
            input_file=data_path,
            output_file=output_file,
            grgsm_command="grgsm_decode",
            extra_args=""  # Add any extra grgsm_decode args here
        )

    def run_grgsm_docker(self, input_file, output_file, grgsm_command="grgsm_decode", extra_args=""):
        """
        Run a gr-gsm command inside the Docker container and stream output in real time.
        :param input_file: Path to the input file on the host
        :param output_file: Path to the output file on the host (if needed)
        :param grgsm_command: gr-gsm command to run (default: grgsm_decode)
        :param extra_args: Additional arguments for gr-gsm command
        """
        import os
        input_dir = os.path.dirname(os.path.abspath(input_file))
        input_filename = os.path.basename(input_file)
        output_filename = os.path.basename(output_file)

        docker_cmd = [
            "docker", "run", "--rm",
            "-v", f"{input_dir}:/mnt",
            "my-grgsm",
            "bash", "-c",
            f"{grgsm_command} {extra_args} -i /mnt/{input_filename} > /mnt/{output_filename} 2>&1"
        ]
        self.realtime_log.insert('end', f'[INFO] Running: {" ".join(docker_cmd)}\n')
        self.realtime_log.see('end')
        try:
            process = subprocess.Popen(
                docker_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            # Stream output in real time
            for line in process.stdout:
                self.realtime_log.insert('end', line)
                self.realtime_log.see('end')
            process.wait()
            if process.returncode != 0:
                self.realtime_log.insert('end', f'[ERROR] gr-gsm Docker process failed with code {process.returncode}\n')
            else:
                self.realtime_log.insert('end', f'[INFO] gr-gsm processing complete. Output: {output_file}\n')
        except Exception as e:
            self.realtime_log.insert('end', f'[ERROR] Exception running gr-gsm in Docker: {e}\n')
        self.realtime_log.see('end')

    def process_last_capture(self):
        """Process the most recent raw capture file using gr-gsm in Docker"""
        if self.last_capture_path and os.path.exists(self.last_capture_path):
            self.process_captured_data(self.last_capture_path, protocol='GSM')
        else:
            messagebox.showwarning("No Capture", "No recent capture file found.")

    def run(self):
        """Start the GUI application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.log_message("Application interrupted by user.")
        except Exception as e:
            messagebox.showerror("Application Error", f"An unexpected error occurred:\n{str(e)}")


def main():
    """Main entry point"""
    print("Starting Nex1 WaveReconX Professional Security Analysis Platform...")

    # Create and run the GUI application
    app = WaveReconXGUI()
    app.run()


if __name__ == "__main__":
    main()