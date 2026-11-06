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


def bt_dang6_p3_b4_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số k để thay đổi độ dài cạnh
                k = random.randint(1, 4)
                # Random 3 trường hợp góc: 1 -> 30 độ, 2 -> 45 độ, 3 -> 60 độ
                choice = random.randint(1, 3)

                # Chiều dài cạnh đáy luôn là 2k*a để khi chia đôi tính trung tuyến không bị lẻ
                base_edge_str = f"{2*k}a"

                if choice == 1:
                    angle = 30
                    height_str = f"{k}a" if k > 1 else "a"
                    tan_val_str = "\\frac{1}{\\sqrt{3}}"
                elif choice == 2:
                    angle = 45
                    height_str = f"{k}\\sqrt{{3}}a" if k > 1 else "\\sqrt{3}a"
                    tan_val_str = "1"
                else:
                    angle = 60
                    height_str = f"{3*k}a" if k > 1 else "3a"
                    tan_val_str = "\\sqrt{3}"

                # Cạnh C'M (đường cao tam giác đều cạnh 2k*a)
                CM_str = f"{k}\\sqrt{{3}}a" if k > 1 else "\\sqrt{3}a"

                # Các đáp án trắc nghiệm
                du = ['$%s^\\circ$' % (angle)]
                da = random.choice(du)

                # Tạo danh sách các góc gây nhiễu
                s = [30, 45, 60, 90]
                s.remove(angle)

                das1 = '$%s^\\circ$' % (s[0])
                das2 = '$%s^\\circ$' % (s[1])
                das3 = '$%s^\\circ$' % (s[2])

                # Câu hỏi
                noidungcauhoi = ('''Cắt đôi khối thủy tinh quang học ở hình dưới theo mặt phẳng $(CA'B')$ tạo ra hai khối lăng kính tam giác, chúng có thể tạo ra các hiệu ứng tán sắc ánh sáng độc đáo chế tác thành các món đồ trang sức bắt mắt. Việc cắt nó đòi hỏi độ chính xác cao cần phải tính được góc phẳng nhị diện $[C, A'B', C']$ để lắp đặt máy cắt.
            \\begin{center}
            \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\tikzset {_d6salnisb/.code = {\\pgfsetadditionalshadetransform{ \\pgftransformshift{\\pgfpoint{0 bp } { 0 bp }  }  \\pgftransformrotate{0 }  \\pgftransformscale{2 }  }}}
            	\\pgfdeclarehorizontalshading{_aoasq1u81}{150bp}{rgb(0bp)=(1,1,0);
            		rgb(37.5bp)=(1,1,0);
            		rgb(62.5bp)=(0.96,0.65,0.14);
            		rgb(100bp)=(0.96,0.65,0.14)}
            	\\tikzset{every picture/.style={line width=0.75pt}} 
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 0; green, 0; blue, 0 }  ,fill opacity=0.29 ] (184.1,251.4) -- (64.1,227.6) -- (98.1,212.1) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.19 ][fill={rgb, 255:red, 215; green, 227; blue, 242 }  ,fill opacity=1 ] (151.5,48) -- (194.1,90.9) -- (186.6,95.4) -- (92.6,76.4) -- cycle ;
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.24 ][fill={rgb, 255:red, 215; green, 227; blue, 242 }  ,fill opacity=1 ] (194.1,90.9) -- (190.1,245.4) -- (184.1,251.4) -- (186.6,95.4) -- cycle ;
            	\\path  [shading=_aoasq1u81,_d6salnisb] (92.6,76.4) -- (186.6,95.4) -- (184.1,251.4) -- (93.1,228.4) -- cycle ; 
            	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.22 ] (92.6,76.4) -- (186.6,95.4) -- (184.1,251.4) -- (93.1,228.4) -- cycle ;  
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 227; blue, 242 }  ,fill opacity=1 ] (129.1,209.4) -- (93.1,228.4) -- (93.1,204.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 215; green, 227; blue, 242 }  ,fill opacity=1 ] (129.1,209.4) -- (184.6,222.4) -- (184.1,251.4) -- (93.1,228.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (124.6,82.9) -- (125.6,208.9) -- (129.1,209.4) -- (128.9,83.9) -- cycle ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (93.6,75.4) -- (187.6,94.4) ;
            	\\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ]   (186.6,95.4) -- (184.1,251.4) ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.46 ] (121.1,82.4) -- (122.1,208.9) -- (125.6,209.4) -- (124.6,82.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.3 ] (129.1,209.4) -- (93.1,228.4) -- (93.1,219.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.21 ] (129.1,209.4) -- (93.1,228.4) -- (116.1,234.4) -- (146.1,212.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.14 ] (129.1,209.4) -- (93.1,181.9) -- (92.6,148.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 155; green, 155; blue, 155 }  ,fill opacity=0.14 ] (129.1,209.4) -- (128.6,85.4) -- (186.6,95.4) -- (184.6,155.4) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (129.1,209.4) -- (125.1,226.9) -- (131.1,223.65) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 245; green, 166; blue, 35 }  ,fill opacity=0.65 ] (194.1,90.9) -- (186.6,95.4) -- (185.6,212.4) -- (191.6,175.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.53 ] (151.5,48) -- (140.6,84.9) -- (194.1,90.9) -- cycle ;
            	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.53 ] (145.6,215.4) -- (141.1,240.4) -- (184.1,251.4) -- (190.1,245.4) -- (188.6,221.9) -- cycle ;
            \\end{tikzpicture} \\hspace{2cm}
            \\begin{tikzpicture}[scale=1, line width=1pt]
            \\coordinate (B) at (0,3.5);
            \\coordinate (C) at (2.5,3);
            \\coordinate (A) at (1.2,4.5);
            \\coordinate (B') at (0,0);
            \\coordinate (C') at (2.5,-0.5);
            \\coordinate (A') at (1.2,1);
            \\draw (A) -- (B) -- (C) -- cycle;
            \\draw (B) -- (B');
            \\draw (C) -- (C');
            \\draw (B') -- (C');
            \\draw[dashed] (A) -- (A');
            \\draw[dashed] (A') -- (B');
            \\draw[dashed] (A') -- (C');
            \\node[above] at (A) {$A$};
            \\node[left] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[right] at (A') {$A'$};
            \\node[left] at (B') {$B'$};
            \\node[right] at (C') {$C'$};
            \\end{tikzpicture}
            \\end{center} Biết khối lăng trụ tam giác đều có cạnh đáy bằng $%s$ và cạnh bên bằng $%s$. Số đo góc phẳng nhị diện $[C, A'B', C']$ theo đơn vị độ bằng bao nhiêu?''' % (base_edge_str, height_str))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[scale=1, line width=1pt]
            \\coordinate (B) at (0,3.5);
            \\coordinate (C) at (2.5,3);
            \\coordinate (A) at (1.2,4.5);
            \\coordinate (B') at (0,0);
            \\coordinate (C') at (2.5,-0.5);
            \\coordinate (A') at (1.2,1);
            \\coordinate (M) at (0.6,0.5);
            \\draw (A) -- (B) -- (C) -- cycle;
            \\draw (B) -- (B');
            \\draw (C) -- (C');
            \\draw (B') -- (C');
            \\draw (C) -- (B');
            \\draw[dashed] (A) -- (A');
            \\draw[dashed] (A') -- (B');
            \\draw[dashed] (A') -- (C');
            \\draw[dashed] (C) -- (A');
            \\draw[dashed] (C') -- (M);
            \\draw[dashed] (C) -- (M);
            \\node[above] at (A) {$A$};
            \\node[left] at (B) {$B$};
            \\node[right] at (C) {$C$};
            \\node[right] at (A') {$A'$};
            \\node[left] at (B') {$B'$};
            \\node[right] at (C') {$C'$};
            \\node[below] at (M) {$M$};
            \\end{tikzpicture}
            \\end{center}
            Gọi $M$ là trung điểm $A'B'$ thì khi đó $C'M \\perp A'B'$ (Do $\\Delta A'B'C'$ là tam giác đều) và $CM \\perp A'B'$ ($\\Delta CA'B'$ cân tại $C$ vì $CA' = CB'$ hai đường chéo của hai hình chữ nhật bằng nhau).\\\\
            Ta có: $\\begin{cases} (A'B'C') \\cap (CA'B') = A'B' \\\\ A'B' \\perp C'M \\subset (A'B'C') \\\\ A'B' \\perp CM \\subset (CA'B') \\end{cases} \\Rightarrow \\left[ (A'B'C'), A'B', (CA'B') \\right] = \\widehat{C'MC}$.\\\\
            Mặt khác: $\\begin{cases} C \\in (CA'B') \\\\ C' \\in (A'B'C') \\end{cases} \\Rightarrow \\left[ C, A'B', C' \\right] = \\left[ (A'B'C'), A'B', (CA'B') \\right] = \\widehat{C'MC}$.\\\\
            Mà $\\Delta A'B'C'$ là tam giác đều cạnh $%s$ nên $C'M = \\frac{%s \\sqrt{3}}{2} = %s$.\\\\
            Xét $\\Delta MCC'$ có $\\widehat{C'} = 90^\\circ$ nên: $\\tan \\widehat{C'MC} = \\frac{CC'}{C'M} = \\frac{%s}{%s} = %s \\Rightarrow \\widehat{C'MC} = %s^\\circ$.''' % (base_edge_str, base_edge_str, CM_str, height_str, CM_str, tan_val_str, angle))
                dapan='\\shortans[0]{$%s$}\n'%(angle)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

