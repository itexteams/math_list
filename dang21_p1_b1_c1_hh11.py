import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang21_p1_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1','2','3']
            dang=random.choice(lisdang)
            if dang=='3':

                #Các đáp án trắc nghiệm
                du = ['$AN$',
                      ]
                da= random.choice(du)
                s = ['$AB$',
                     '$AC$',
                     '$AD$',
                     '$AG$',
                     '$AM$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm của tam giác $BCD$, $M, N$ là trung điểm của $BC, CD$. Giao tuyến của mặt phẳng $(ACD)$ và $(ABG)$ là'''
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
            		\\coordinate (A) at (2,3);
            		\\coordinate (B) at (0,0);
            		\\coordinate (C) at (1,-2);
            		\\coordinate (D) at (4,0);
            		\\coordinate (M) at (0.5,-1); 
            		\\coordinate (N) at (2.5,-1);  
            		\\coordinate (G) at (1.7,-0.6);  
            		\\draw[line width=1pt,dashed] (B)--(D);
            		\\draw[line width=1pt,dashed] (A)--(G);
            		\\draw[line width=1pt,dashed] (B)--(N);
            		\\draw[line width=1pt,dashed] (D)--(M);
            		\\draw[line width=1pt] (A)--(B);
            		\\draw[line width=1pt] (A)--(C);
            		\\draw[line width=1pt] (A)--(D);
            		\\draw[line width=1pt] (B)--(C)--(D);
            		\\draw[line width=1pt] (A)--(M);
            		\\draw[line width=1pt] (A)--(N);
            		\\node[above] at (A) {$A$};
            		\\node[left] at (B) {$B$};
            		\\node[below] at (C) {$C$};
            		\\node[right] at (D) {$D$};
            		\\node[below left] at (M) {$M$};
            		\\node[below right] at (N) {$N$};
            		\\node[below] at (G) {$G$};
            	\\end{tikzpicture}
            \\end{center}
            Ta có $(ACD) \\cap (AGG)=AN$.'''

                         %(
                         ))
            if dang=='2':

                #Các đáp án trắc nghiệm
                du = ['$AM$',
                      ]
                da= random.choice(du)
                s = ['$AB$',
                     '$AC$',
                     '$AD$',
                     '$AG$',
                     '$AN$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm của tam giác $BCD$, $M, N$ là trung điểm của $BC, CD$. Giao tuyến của mặt phẳng $(ABC)$ và $(ADG)$ là'''
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
            		\\coordinate (A) at (2,3);
            		\\coordinate (B) at (0,0);
            		\\coordinate (C) at (1,-2);
            		\\coordinate (D) at (4,0);
            		\\coordinate (M) at (0.5,-1); 
            		\\coordinate (N) at (2.5,-1);  
            		\\coordinate (G) at (1.7,-0.6);  
            		\\draw[line width=1pt,dashed] (B)--(D);
            		\\draw[line width=1pt,dashed] (A)--(G);
            		\\draw[line width=1pt,dashed] (B)--(N);
            		\\draw[line width=1pt,dashed] (D)--(M);
            		\\draw[line width=1pt] (A)--(B);
            		\\draw[line width=1pt] (A)--(C);
            		\\draw[line width=1pt] (A)--(D);
            		\\draw[line width=1pt] (B)--(C)--(D);
            		\\draw[line width=1pt] (A)--(M);
            		\\draw[line width=1pt] (A)--(N);
            		\\node[above] at (A) {$A$};
            		\\node[left] at (B) {$B$};
            		\\node[below] at (C) {$C$};
            		\\node[right] at (D) {$D$};
            		\\node[below left] at (M) {$M$};
            		\\node[below right] at (N) {$N$};
            		\\node[below] at (G) {$G$};
            	\\end{tikzpicture}
            \\end{center}
            Ta có $(ABC) \\cap (ADG)=AM$.'''

                         %(
                         ))
            if dang=='1':

                #Các đáp án trắc nghiệm
                du = ['$AG$',
                      ]
                da= random.choice(du)
                s = ['$AB$',
                     '$AC$',
                     '$AD$',
                     '$AM$',
                     '$AN$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho tứ diện $ABCD$, $G$ là trọng tâm của tam giác $BCD$, $M, N$ là trung điểm của $BC, CD$. Giao tuyến của mặt phẳng $(ABN)$ và $(ADM)$ là'''
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
            		\\coordinate (A) at (2,3);
            		\\coordinate (B) at (0,0);
            		\\coordinate (C) at (1,-2);
            		\\coordinate (D) at (4,0);
            		\\coordinate (M) at (0.5,-1); 
            		\\coordinate (N) at (2.5,-1);  
            		\\coordinate (G) at (1.7,-0.6);  
            		\\draw[line width=1pt,dashed] (B)--(D);
            		\\draw[line width=1pt,dashed] (A)--(G);
            		\\draw[line width=1pt,dashed] (B)--(N);
            		\\draw[line width=1pt,dashed] (D)--(M);
            		\\draw[line width=1pt] (A)--(B);
            		\\draw[line width=1pt] (A)--(C);
            		\\draw[line width=1pt] (A)--(D);
            		\\draw[line width=1pt] (B)--(C)--(D);
            		\\draw[line width=1pt] (A)--(M);
            		\\draw[line width=1pt] (A)--(N);
            		\\node[above] at (A) {$A$};
            		\\node[left] at (B) {$B$};
            		\\node[below] at (C) {$C$};
            		\\node[right] at (D) {$D$};
            		\\node[below left] at (M) {$M$};
            		\\node[below right] at (N) {$N$};
            		\\node[below] at (G) {$G$};
            	\\end{tikzpicture}
            \\end{center}
            Ta có $(ABN) \\cap (ADM)=AG$.'''

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

