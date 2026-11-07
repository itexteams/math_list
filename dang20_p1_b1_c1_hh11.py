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


def bt_dang20_p1_b1_c1_hh11(self):
                # Khai báo biến
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                
                if dang=='1':
                    #Khai báo biến
                    n=randint(3,9)
                    kq=math.comb(n, 2)
                    #Các đáp án trắc nghiệm
                    du = ['Tạo thành một hình tứ diện',
                          ]
                    da= random.choice(du)
                    s = ['Tạo thành một hình tứ giác',
                         'Thẳng hàng',
                         'Chỉ có $3$ trong $4$ điểm thẳng hàng',
                         'cùng thuộc một đường tròn',
                        ]
                
                    das1 = random.choice(s)
                    s.remove(das1)
                    das2 = random.choice(s)
                    s.remove(das2)
                    das3 = random.choice(s)
                    # Câu hỏi
                    noidungcauhoi = ('''Trong không gian, cho hai hình bình hành $ABCD$ và $ACNM$. Khi đó có thể kết luận gì về bốn điểm $B, M, D, N$'''
                                     %(
                                     ))
                    # Các đáp án
                    da_d = ('\\True ' +str(da))
                    da_s1 = str(das1)
                    da_s2 = str(das2) 
                    da_s3 = str(das3) 
                    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                    list_1 = [da_d,da_s1,da_s2,da_s3]
                    random.shuffle(list_1)
                    # Nội dung lời giải
                    loigiai=('''\\begin{center}
	\\begin{tikzpicture}
		\\coordinate (A) at (0,0);
		\\coordinate (B) at (-3,-1.5);
		\\coordinate (C) at (3,-1.5);
		\\coordinate (D) at (6,0);
		\\coordinate (M) at (-1.5,3.5);
		\\coordinate (N) at (1.5,1.5);
		\\coordinate (X) at (1.51,-0.75);
		\\coordinate (Y) at (2.5,-0.58);
		\\coordinate (Z) at (2.25,0);
		\\draw[line width=1pt,dashed] (A)--(D);
		\\draw[line width=1pt,dashed] (B)--(D);
		\\draw[line width=1pt] (A)--(B);
		\\draw[line width=1pt] (B)--(C);
		\\draw[line width=1pt] (C)--(D);
		\\draw[line width=1pt] (A)--(C);
		\\draw[line width=1pt] (M)--(A);
		\\draw[line width=1pt] (M)--(N);
		\\draw[line width=1pt] (N)--(C);
		\\draw[line width=1pt] (B)--(X);
		\\draw[line width=1pt] (D)--(Y);
		\\draw[line width=1pt] (D)--(Z);
		\\node[left] at (A) {$A$};
		\\node[left] at (B) {$B$};
		\\node[below right] at (C) {$C$};
		\\node[right] at (D) {$D$};
		\\node[above] at (M) {$M$};
		\\node[above right] at (N) {$N$};
	\\end{tikzpicture}
\\end{center}
Vì $ABCD$ và $ACNM$ là hai hình bình hành chỉ có chung đường chéo $AC$ nên $B, D, N, M$ không đồng phẳng. \\\\
                             Mà $MN//AC$ còn $AC$ cắt $BD$ nên $BD$ và $MN$ chéo nhau. Vậy bốn điểm $B, M, D, N$ tạo thành một hình tứ diện.''' 
                             %(
                             ))
                
                
                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                    '\\choice \n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '{'+str(list_1[0])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('+-','-')
                return content