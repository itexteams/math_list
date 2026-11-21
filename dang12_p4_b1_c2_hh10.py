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


def bt_dang12_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random tên các điểm cho ngũ giác
        list_ngu_giac = [("A", "B", "C", "D", "E"), ("M", "N", "P", "Q", "R"), ("U", "V", "X", "Y", "Z")]
        ngu_giac = random.choice(list_ngu_giac)
        T1, T2, T3, T4, T5 = ngu_giac
        
        # Đặt tên các trung điểm cố định theo yêu cầu (không random điểm)
        M, N, P, Q_td = "M", "N", "P", "Q"
        I, J = "I", "J"
        K = "K" # Điểm lấy thêm
    
        # Đảm bảo các trung điểm không trùng tên với đỉnh ngũ giác (nếu cần thiết, nhưng đề bài yêu cầu không random điểm, ta dùng tên đỉnh A, B, C, D, E và trung điểm M, N, P, Q)
        # Để an toàn và bám sát mẫu 100%, ta sẽ cố định tên các điểm như trong hình "image_f45104.png".
        
        T1, T2, T3, T4, T5 = "A", "B", "C", "D", "E"
        M, N, P, Q_td = "M", "N", "P", "Q"
        I, J = "I", "J"
        K = "K"
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho ngũ giác lồi $%s %s %s %s %s$. Gọi $%s, %s, %s, %s$ lần lượt là trung điểm của $%s %s, %s %s, %s %s, %s %s$. Gọi $%s, %s$ lần lượt là trung điểm của $%s %s$ và $%s %s$. Chứng minh rằng vectơ $\\overrightarrow{%s %s}$ cùng phương với $\\overrightarrow{%s %s}$ và $|\\overrightarrow{%s %s}| = \\frac{1}{4}|\\overrightarrow{%s %s}|$.'
                         %(T1, T2, T3, T4, T5, M, N, P, Q_td, T1, T2, T2, T3, T3, T4, T4, T5, I, J, M, P, N, Q_td, I, J, T1, T5, I, J, T1, T5))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Lấy $%s$ là trung điểm của $%s %s$. \n'
                   '\\item Chứng minh $%s %s %s %s$ là hình bình hành (do $%s %s \\parallel %s %s, %s %s = \\frac{1}{2} %s %s$ và $%s %s \\parallel %s %s, %s %s = \\frac{1}{2} %s %s$). \n'
                   '\\item Suy ra trung điểm $%s$ của $%s %s$ cũng là trung điểm của $%s %s$. \n'
                   '\\item Xét $\\triangle %s %s %s$ có $%s$ là trung điểm $%s %s$, $%s$ là trung điểm $%s %s \\Rightarrow %s %s$ là đường trung bình $\\Rightarrow %s %s \\parallel %s %s$ và $%s %s = \\frac{1}{2} %s %s$. \n'
                   '\\item Trong $\\triangle %s %s %s, %s %s$ là đường trung bình $\\Rightarrow %s %s \\parallel %s %s \\dots$ (Lưu ý: Để chuẩn xác hơn là chứng minh $%s %s$ cùng phương với $%s %s$ nếu thứ tự đỉnh phù hợp; với giả thiết trên, $%s %s \\parallel %s %s$ nên $\\overrightarrow{%s %s}$ cùng phương với $\\overrightarrow{%s %s}$ và $|\\overrightarrow{%s %s}| = \\frac{1}{4}|\\overrightarrow{%s %s}|$).\n'
                   '\\end{itemize}'
                   %(K, T2, T4, M, K, P, N, M, K, T1, T4, M, K, T1, T4, N, P, T1, T4, N, P, T1, T4, I, M, P, N, K, N, K, Q_td, I, N, K, J, N, Q_td, I, J, I, J, K, Q_td, I, J, K, Q_td, T2, T4, T5, K, Q_td, K, Q_td, T2, T5, I, J, T1, T5, K, Q_td, T2, T5, I, J, T2, T5, I, J, T2, T5))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

