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


def bt_dang12_p3_b5_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Suy nghĩ tìm cách random bài toán
                # Sử dụng các bộ số Pitago để kết quả AC là số nguyên cho đẹp, hoặc random số tự nhiên
                triples = [(3, 4), (6, 8), (5, 12), (9, 12), (8, 15), (12, 16), (7, 24), (20, 21)]
                a, b = random.choice(triples)
                # Có thể hoán vị a và b
                if random.randint(0, 1) == 0:
                    a, b = b, a

                # Tính toán các thông số
                # Khoảng cách d(BB', AC') = d(B, AC) trong tam giác vuông ABC
                ac_sq = a**2 + b**2
                ac = int(math.sqrt(ac_sq))

                # Khoảng cách h = (a*b)/ac
                kq_num = a * b
                kq_den = ac

                # Chuyển sang số thập phân và định dạng dấu phẩy
                kq_val = float(kq_num) / kq_den
                kq_str = str(round(kq_val, 2)).replace('.', ',')
                if kq_str.endswith(',0'):
                    kq_str = kq_str.replace(',0', '')

                # Đáp án đúng
                da = '$%s$' % kq_str

                # Bước 4: Điều chỉnh các phương án sai không được trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai_val = round(kq_val + random.choice([-1.5, -1, -0.5, 0.5, 1, 1.5, 2]), 1)
                    if sai_val > 0:
                        sai_str = '$%s$' % (str(sai_val).replace('.', ','))
                        if sai_str != da and sai_str not in s:
                            s.append(sai_str)

                das1, das2, das3 = s

                # Câu hỏi (B2 - Viết lại y hệt cấu trúc đề bài)
                noidungcauhoi = ('''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = %s, BC = %s$. Khoảng cách giữa hai đường thẳng $BB'$ và $AC'$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(a), latex(b)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết (B2 - Không viết tắt, trình bày rõ ràng)
                loigiai = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (87.47,65.4) -- (87.47,165.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.47,25.4) -- (127.47,125.4) ;
            		\draw [line width=1]    (247.47,25.4) -- (247.47,125.4) ;
            		\draw [line width=1]    (207.47,65.4) -- (207.47,165.4) ;
            		\draw [line width=1]    (87.47,65.4) -- (127.47,25.4) ;
            		\draw [line width=1]    (207.47,65.4) -- (247.47,25.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (87.47,165.4) -- (127.47,125.4) ;
            		\draw [line width=1]    (207.47,165.4) -- (247.47,125.4) ;
            		\draw [line width=1]    (87.47,65.4) -- (207.47,65.4) ;
            		\draw [line width=1]    (127.47,25.4) -- (247.47,25.4) ;
            		\draw [line width=1]    (87.47,165.4) -- (207.47,165.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (127.47,125.4) -- (247.47,125.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (207.47,65.4) -- (127.47,125.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (207.47,165.4) -- (127.47,125.4) ;
            		\draw [line width=1]    (127.47,25.4) -- (207.47,65.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (150.47,136.4) -- (87.47,165.4) ;
            		\draw (105,108) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (72,164) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (207.47,165.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (249,113) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (108,5) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            		\draw (66,53) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            		\draw (207.47,65.4) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            		\draw (249,13) node [anchor=north west][inner sep=0.75pt]    {$D'$};
            		\draw (140,140) node [anchor=north west][inner sep=0.75pt]    {$H$};
            	\end{tikzpicture} 
            \end{center}'''
                    '''Trong hình hộp chữ nhật $ABCD.A'B'C'D'$, ta có $BB' \\parallel AA'$. \\\\
                             Mà $AA' \\subset \\left(ACC'A'\\right)$ nên $BB' \\parallel \\left(ACC'A'\\right)$. \\\\
                             Vì đường thẳng $AC'$ nằm trong mặt phẳng $\\left(ACC'A'\\right)$ nên khoảng cách giữa hai đường thẳng $BB'$ và $AC'$ là: \\\\
                             $d\\left(BB', AC'\\right) = d\\left(BB', \\left(ACC'A'\\right)\\right) = d\\left(B, \\left(ACC'A'\\right)\\right)$. \\\\
                             Vì $BB' \\perp \\left(ABCD\\right)$ nên mặt phẳng $\\left(ACC'A'\\right) \\perp \\left(ABCD\\right)$ theo giao tuyến $AC$. \\\\
                             Trong mặt phẳng $\\left(ABCD\\right)$, kẻ $BH \\perp AC$ tại $H$. Khi đó $BH \\perp \\left(ACC'A'\\right)$. \\\\
                             Suy ra $d\\left(B, \\left(ACC'A'\\right)\\right) = BH$. \\\\
                             Xét tam giác $ABC$ vuông tại $B$, ta có: \\\\
                             $AC = \\sqrt{AB^2 + BC^2} = \\sqrt{%s^2 + %s^2} = %s$. \\\\
                             Chiều cao $BH$ của tam giác vuông $ABC$ được tính bởi công thức: \\\\
                             $BH = \\frac{AB \\cdot BC}{AC} = \\frac{%s \\cdot %s}{%s} = %s$. \\\\
                             Vậy khoảng cách cần tìm là $%s$.'''
                           % (latex(a), latex(b), latex(ac),
                              latex(a), latex(b), latex(ac), latex(Rational(kq_num, kq_den)),
                              kq_str))
                dapan=' \\shortans[0]{$%s$} '%(kq_str)  
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

