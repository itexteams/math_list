import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang14_p4_b1_c1_hh11(self):
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                if dang=='1':
                                    
                    # Câu hỏi
                    noidungcauhoi = ('''Trong không gian, cho hình chóp $S.ABC$, gọi $M, N, P$ thuộc các cạnh $SA, SB, SC$ sao cho $MN, NP$ và $PM$ cắt mặt phẳng $(ABC)$ tương ứng tại các điểm $D, E, F$. Chứng mình $D, E, F$ thẳng hàng.'''
                    )
                
                    # Nội dung lời giải
                    loigiai = ('''\\begin{center}
	\\begin{tikzpicture}
		\\coordinate (S) at (0, 3.5);
		\\coordinate (B) at (0, -3);
		\\coordinate (N) at (0, 1);       
		\\coordinate (D) at (-4, 0);    
		\\coordinate (A) at ($(D)!0.5!(B)$); 
		\\coordinate (M) at (intersection of S--A and D--N);
		\\coordinate (base_left) at (-5, -1.5); 
		\\coordinate (F) at (7, -1.5);          
		\\coordinate (C) at (3, -1.5);         
		\\coordinate (P) at (intersection of S--C and M--F);
		\\coordinate (E) at (intersection of B--C and D--F);
		\\draw[line width=1pt, dashed] (A)--(C);      
		\\draw[line width=1pt, dashed] (M)--(P);      
		\\draw[line width=1pt, dashed] (D)--(F);       
		\\draw[line width=1pt] (S)--(A);   
		\\draw[line width=1pt, dashed] (P)--(E);  
		\\draw[line width=1pt, dashed] (C)--(E);     
		\\draw[line width=1pt] (S)--(B);              
		\\draw[line width=1pt] (S)--(C);               
		\\draw[line width=1pt] (S)--(D);           
		\\draw[line width=1pt] (D)--(A);             
		\\draw[line width=1pt] (A)--(B);             
		\\draw[line width=1pt] (B)--(C);            
		\\draw[line width=1pt] (C)--(F);              
		\\draw[line width=1pt] (P)--(F);              
		\\draw[line width=1pt] (D)--(M)--(N)--(P);    
		\\draw[line width=1pt] (S)--(M);              
		\\draw[line width=1pt] (N)--(B);           
		\\node[above] at (S) {$S$};
		\\node[above left] at (M) {$M$};
		\\node[above right] at (N) {$N$};
		\\node[above right] at (P) {$P$};
		\\node[left] at (D) {$D$};
		\\node[below left] at (A) {$A$};
		\\node[below] at (B) {$B$};
		\\node[below] at (C) {$C$};
		\\node[below] at (E) {$E$};
		\\node[right] at (F) {$F$};
	\\end{tikzpicture}
\\end{center}
Ba mặt phẳng $(ABC), (SAC)$ và $(DNE)$ đồng quy. \\\\
                               Ta có $\\heva{&(ABC) \\cap (SAC)=AC\\\\&(SAC) \\cap (DNE)=MP\\\\&(DNE) \\cap (ABC)=DE}$ nên các đường thẳng $AC, MP, DE$ đồng quy. \\\\
                                   Mà $AC \\cap MP=F$ nên $F \\in DE$. Vậy ba điểm $D, E, F$ thẳng hàng.''')
                
                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+
                    '\\loigiai{ \n'
                    +str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
                return content 