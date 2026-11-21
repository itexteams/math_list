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


def bt_dang4_p4_b1_c2_hh10(self):
    # Khai báo biến
    
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        # Random tên các điểm để bài toán đa dạng
        diem_giac = random.choice([("A", "B", "C"), ("M", "N", "P"), ("D", "E", "F")])
        D1, D2, D3 = diem_giac
        
        # Các điểm đặc biệt
        truc_tam = random.choice(["H", "K", "T"])
        trong_tam = random.choice(["G", "S"])
        tam_ngoai_tiep = random.choice(["O", "I"])
        diem_doi_xung = random.choice(["D", "Q", "R"])
        
        # Đảm bảo điểm đối xứng khác với các điểm đã có
        while diem_doi_xung in [D1, D2, D3, truc_tam, trong_tam, tam_ngoai_tiep]:
            diem_doi_xung = random.choice(["D", "Q", "R", "X", "Y", "Z"])
    
        # Nội dung câu hỏi
        noidungcauhoi = ('Cho tam giác $%s %s %s$ có trực tâm $%s$, trọng tâm $%s$ và tâm đường tròn ngoại tiếp $%s$. Gọi $%s$ là điểm đối xứng với $%s$ qua $%s$. Chứng minh rằng $\\overrightarrow{%s %s} = \\overrightarrow{%s %s}$ và $\\overrightarrow{%s %s} = \\overrightarrow{%s %s}$.'
                         %(D1, D2, D3, truc_tam, trong_tam, tam_ngoai_tiep, diem_doi_xung, D1, tam_ngoai_tiep, D2, truc_tam, diem_doi_xung, D3, D3, truc_tam, diem_doi_xung, D2))
        
        # Nội dung lời giải
        loigiai = ('\\begin{itemize} \n'
                   '\\item Vì $%s %s$ là đường kính của $(%s)$ nên $\\widehat{%s %s %s} = \\widehat{%s %s %s} = 90^\\circ \\Rightarrow %s %s \\perp %s %s$ và $%s %s \\perp %s %s$. \n'
                   '\\item Mặt khác, $%s$ là trực tâm $\\triangle %s %s %s$ nên $%s %s \\perp %s %s$ và $%s %s \\perp %s %s$. \n'
                   '\\item Suy ra $%s %s \\parallel %s %s$ và $%s %s \\parallel %s %s$, do đó tứ giác $%s %s %s %s$ là hình bình hành. \n'
                   '\\item Từ tính chất hình bình hành, ta có $\\overrightarrow{%s %s} = \\overrightarrow{%s %s}$ và $\\overrightarrow{%s %s} = \\overrightarrow{%s %s}$. \n'
                   '\\end{itemize}'
                   %(D1, diem_doi_xung, tam_ngoai_tiep, D1, D3, diem_doi_xung, D1, D2, diem_doi_xung, diem_doi_xung, D3, D1, D3, diem_doi_xung, D2, D1, D2, truc_tam, D1, D2, D3, D2, truc_tam, D1, D3, D3, truc_tam, D1, D2, D2, truc_tam, diem_doi_xung, D3, D3, truc_tam, diem_doi_xung, D2, D2, truc_tam, D3, diem_doi_xung, D2, truc_tam, diem_doi_xung, D3, D3, truc_tam, diem_doi_xung, D2))
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
               '\\loigiai{ \n' +str(loigiai)+'\n}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content      

