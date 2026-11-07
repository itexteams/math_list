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


def bt_dang13_p3_b4_c4_ds10(self):
    # Khai báo biến
    # Khai báo biến và chọn dạng
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        # Thiết lập các bộ số (m, n, L) sao cho x = (n*L) / sqrt(m^2 - n^2) là số nguyên
        # Bộ (3, 4, 5): m=5, n=3, sqrt=4. L chia hết cho 4.
        # Bộ (5, 12, 13): m=13, n=5, sqrt=12. L chia hết cho 12.
        # Bộ (8, 15, 17): m=17, n=8, sqrt=15. L chia hết cho 15.
        danh_sach_bo_so = [
            {'m': 5, 'n': 3, 'L': 4},
            {'m': 5, 'n': 3, 'L': 8},
            {'m': 5, 'n': 3, 'L': 12},
            {'m': 13, 'n': 5, 'L': 12},
            {'m': 17, 'n': 8, 'L': 15},
            {'m': 10, 'n': 6, 'L': 8}
        ]
        
        bo_chon = random.choice(danh_sach_bo_so)
        m = bo_chon['m']
        n = bo_chon['n']
        L = bo_chon['L']
        
        # Tính toán các giá trị trung gian cho lời giải
        L2 = L**2
        m2 = m**2
        n2 = n**2
        hieu_binh_phuong = m2 - n2
        
        # Tính đáp án đúng x (AB)
        kq_x = (n * L) // int(math.sqrt(hieu_binh_phuong))
        da_dung = '$%s$m' % (latex(kq_x))
    
        # Tạo các phương án sai (đảm bảo không trùng đáp án đúng và là số dương)
        s = []
        while len(s) < 3:
            sai = kq_x + random.choice([-3, -2, -1, 1, 2, 3, 4, 5])
            if sai > 0 and sai != kq_x and ('$%s$m' % (latex(sai))) not in s:
                s.append('$%s$m' % (latex(sai)))
    
        # Câu hỏi
        noidungcauhoi = ('''Người ta làm ra một cái thang bắc lên tầng hai của một ngôi nhà, muốn vậy họ cần làm một thanh đỡ $BC$ có chiều dài bằng $%s$m, đồng thời muốn đảm bảo kỹ thuật thì tỉ số độ dài $\\frac{CE}{BD} = \\frac{%s}{%s}$. 
                        \\begin{center}
	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=0.34 ] (381.47,120) -- (241.47,120) -- (241.47,239.07) -- (381.47,239.07) -- cycle ;
		\\draw  [fill={rgb, 255:red, 208; green, 2; blue, 27 }  ,fill opacity=0.34 ] (312.47,80) -- (381.47,120.07) -- (241.47,120.07) -- cycle ;
		\\draw    (121.47,239.07) -- (241.47,239.07) ;
		\\draw    (121.47,239.07) -- (241.47,179.07) ;
		\\draw    (181.47,209.07) -- (181.47,239.07) ;
		\\draw    (381.47,179.07) -- (241.47,179.07) ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (261.37,178.52) -- (261.4,160.68) .. controls (261.41,150.83) and (270.01,142.86) .. (280.59,142.88) .. controls (291.17,142.89) and (299.74,150.89) .. (299.72,160.74) -- (299.7,178.58) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (321.42,178.75) -- (321.45,160.29) .. controls (321.47,150.09) and (330.5,141.84) .. (341.62,141.86) .. controls (352.74,141.87) and (361.75,150.15) .. (361.73,160.35) -- (361.7,178.81) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (361.43,239.24) -- (261.47,239.07) -- (261.52,206.57) -- (311.52,199.15) -- (361.49,206.74) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (264.24,178.56) -- (264.26,162.04) .. controls (264.28,152.92) and (271.59,145.53) .. (280.59,145.55) .. controls (289.59,145.56) and (296.87,152.97) .. (296.86,162.09) -- (296.83,178.61) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (325.27,178.56) -- (325.29,161.84) .. controls (325.31,152.61) and (332.62,145.14) .. (341.62,145.15) .. controls (350.62,145.16) and (357.9,152.66) .. (357.89,161.89) -- (357.86,178.61) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (359.25,238.67) -- (263.65,238.5) -- (263.7,208.41) -- (311.51,201.55) -- (359.3,208.58) -- cycle ;
		\\draw (104.18,238.2) node [anchor=north west][inner sep=0.75pt]    {$A$};
		\\draw (172.84,239.87) node [anchor=north west][inner sep=0.75pt]    {$B$};
		\\draw (170.84,186.87) node [anchor=north west][inner sep=0.75pt]    {$C$};
		\\draw (230.18,238.53) node [anchor=north west][inner sep=0.75pt]    {$D$};
		\\draw (224.18,158.53) node [anchor=north west][inner sep=0.75pt]    {$E$};
	\\end{tikzpicture}
\\end{center} Hỏi vị trí $A$ cách vị trí $B$ bao nhiêu mét?'''% (latex(L), latex(m), latex(n)))
    
        # Các đáp án
        da_d = ('\\True ' + str(da_dung))
        da_s1 = str(s[0])
        da_s2 = str(s[1])
        da_s3 = str(s[2])
    
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
    
        # Nội dung lời giải chi tiết
        loigiai = ('''Đặt $AB = x > 0$. Xét tam giác $ABC$ vuông tại $B$ có: $AC = \\sqrt{x^2 + %s}$. \\\\
                     Theo tính chất định lí Ta-lét, ta có: $\\frac{AC}{AB} = \\frac{CE}{BD} \\Leftrightarrow \\frac{\\sqrt{x^2 + %s}}{x} = \\frac{%s}{%s}$ \\\\
                     $\\Leftrightarrow %s\\sqrt{x^2 + %s} = %sx \\Leftrightarrow \\begin{cases} %sx \\ge 0 \\\\ %s(x^2 + %s) = %sx^2 \\end{cases}$ \\\\
                     $\\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ %sx^2 + %s = %sx^2 \\end{cases} \\Leftrightarrow \\begin{cases} x \\ge 0 \\\\ %sx^2 = %s \\end{cases} \\Leftrightarrow x = %s$. \\\\
                     Vậy hai vị trí $A, B$ cách nhau $%s$m.'''
                   % (latex(L2), latex(L2), latex(m), latex(n),
                      latex(n), latex(L2), latex(m), 
                      latex(m), latex(n2), latex(L2), latex(m2),
                      latex(n2), latex(n2*L2), latex(m2),
                      latex(hieu_binh_phuong), latex(n2*L2), latex(kq_x),
                      latex(kq_x)
                      ))
        #Đáp án
        dapan='\\shortans[0]{$%s$}\n'%(latex(kq_x))
    
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
               '\\loigiai{' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content