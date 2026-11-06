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


def bt_dang33_p3_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B1 & B3: Nghiên cứu đề bài và thiết lập random
                # h_cong: chiều cao cổng (trong ảnh là 4)
                # w_cua, h_cua: kích thước cửa giữa (trong ảnh là 3x4)
                # Lưu ý: Để bài toán hợp lý, h_cua < h_cong. Trong ảnh mẫu h_cua=3, h_cong=4

                h_cong = random.randint(4, 10) 
                h_cua = h_cong - random.randint(1, 2)
                w_cua = random.randint(2, 6)

                # B2: Giải chi tiết theo Sympy để lấy kết quả chính xác
                # Gắn hệ trục tọa độ sao cho đỉnh G(0; h_cong) => (P): y = ax^2 + h_cong
                # Điểm E nằm trên cửa chính có tọa độ (w_cua/2 ; h_cua)
                xE = Rational(w_cua, 2)
                yE = h_cua

                # Tìm hệ số a: yE = a*xE^2 + h_cong => a = (yE - h_cong) / xE^2
                a_val = Rational(yE - h_cong, xE**2)

                # Tìm giao điểm AB với trục hoành (y=0): ax^2 + h_cong = 0 => x^2 = -h_cong/a
                x_sq = Rational(-h_cong, a_val)
                khoang_cach_AB = 2 * (x_sq**0.5)

                # Chuyển kết quả sang số thập phân và làm tròn 1 chữ số (hoặc tùy ý)
                # Ở đây tôi làm tròn theo yêu cầu giống mẫu 
                kq_num = float(khoang_cach_AB)
                kq_dec = Decimal(str(kq_num)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

                # Chuyển dấu chấm thành dấu phẩy cho đúng định dạng tiếng Việt
                da_dung = str(kq_dec).replace('.', ',')

                # B4: Tạo các phương án sai không trùng đáp án đúng
                s = []
                while len(s) < 3:
                    sai_val = kq_dec + Decimal(str(random.choice([-2, -1.5, -1, 1, 1.5, 2, 3])))
                    if sai_val > 0:
                        sai_str = str(sai_val).replace('.', ',')
                        if sai_str != da_dung and sai_str not in s:
                            s.append(sai_str)

                das1, das2, das3 = s[0], s[1], s[2]

                # Nội dung câu hỏi
                noidungcauhoi = ('''Một chiếc cổng hình parabol bao gồm một cửa chính hình chữ nhật ở giữa và hai cánh cửa phụ hai bên như hình vẽ. 
                                 \\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw   (311.04,171) .. controls (242.95,20.84) and (174.3,20.58) .. (105.06,170.21) ;
            		\\draw    (105.06,170.21) -- (311.04,171) ;
            		\\draw   (154.47,89.73) -- (262.47,89.73) -- (262.47,170.61) -- (154.47,170.61) -- cycle ;
            		\\draw (87,170.33) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (311.04,171) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (146,173.33) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\\draw (254,174.33) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\\draw (265,68.33) node [anchor=north west][inner sep=0.75pt]    {$E$};
            		\\draw (137,67.33) node [anchor=north west][inner sep=0.75pt]    {$F$};
            		\\draw (200,33.33) node [anchor=north west][inner sep=0.75pt]    {$G$};
            	\\end{tikzpicture}
            \\end{center} Biết chiều cao cổng parabol là $%sm$ còn kích thước cửa ở giữa là $%sm \\times %sm$. Khoảng cách giữa hai điểm $A$ và $B$ bằng bao nhiêu mét? (làm tròn đến hàng đơn vị).'''
                                 %(latex(h_cong), latex(w_cua), latex(h_cua)))

                # Nội dung lời giải chi tiết y hệt mẫu ảnh
                loigiai = ('''\\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw   (311.04,171) .. controls (242.95,20.84) and (174.3,20.58) .. (105.06,170.21) ;
            		\\draw    (105.06,170.21) -- (311.04,171) ;
            		\\draw   (154.47,89.73) -- (262.47,89.73) -- (262.47,170.61) -- (154.47,170.61) -- cycle ;
            		\\draw    (81.47,169.73) -- (348.47,170.73) ;
            		\\draw [shift={(350.47,170.73)}, rotate = 180.21] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\\draw    (208.47,202.17) -- (208.47,10.17) ;
            		\\draw [shift={(208.47,8.17)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            		\\draw (88,174.33) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (311.04,179) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (145,177.33) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\\draw (254,178.33) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\\draw (265,68.33) node [anchor=north west][inner sep=0.75pt]    {$E$};
            		\\draw (137,67.33) node [anchor=north west][inner sep=0.75pt]    {$F$};
            		\\draw (184,37.33) node [anchor=north west][inner sep=0.75pt]    {$G$};
            		\\draw (187,176) node [anchor=north west][inner sep=0.75pt]    {$O$};
            		\\draw (333,147) node [anchor=north west][inner sep=0.75pt]    {$x$};
            		\\draw (189,4) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\\end{tikzpicture}
            \\end{center} Gắn hệ trục tọa độ $Oxy$ như hình vẽ, chiếc cổng là một phần của parabol $(P)$: $y = ax^2 + bx + c$ với $a < 0$. \\\\
            Do parabol $(P)$ đối xứng qua trục tung nên có trục đối xứng $x = 0 \\Rightarrow -\\frac{b}{2a} = 0 \\Leftrightarrow b = 0$. \\\\
            Chiều cao của cổng parabol là $%sm$ nên $G(0; %s) \\Rightarrow c = %s$. \\\\
            $\\Rightarrow (P): y = ax^2 + %s$ \\\\
            Lại có, kích thước cửa ở giữa là $%sm \\times %sm$ nên $E(%s; %s), F(-%s; %s)$ \\\\
            $\\Rightarrow %s = a(%s)^2 + %s \\Leftrightarrow a = %s$. \\\\
            Vậy $(P): y = %sx^2 + %s$. \\\\
            Ta có $%sx^2 + %s = 0 \\Leftrightarrow x^2 = %s \\Leftrightarrow \\left[\\begin{matrix} x = %s \\\\ x = -%s \\end{matrix}\\right.$ nên $A(-%s; 0), B(%s; 0)$ hay $AB = %s$ (m).'''
                           %(latex(h_cong), latex(h_cong), latex(h_cong),
                             latex(h_cong), 
                             latex(w_cua), latex(h_cua), latex(float(xE)).replace('.',','), latex(h_cua), latex(float(xE)).replace('.',','), latex(h_cua),
                             latex(h_cua), latex(float(xE)).replace('.',','), latex(h_cong), latex(a_val),
                             latex(a_val), latex(h_cong),
                             latex(a_val), latex(h_cong), latex(x_sq), latex(float(x_sq**0.5)).replace('.',','), latex(float(x_sq**0.5)).replace('.',','),
                             latex(float(x_sq**0.5)).replace('.',','), latex(float(x_sq**0.5)).replace('.',','), da_dung))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(latex(da_dung))

                # Đưa các đáp án vào danh sách
                da_d = ('\\True $%s$m' % da_dung)
                list_1 = [da_d, '$%s$m' % das1, '$%s$m' % das2, '$%s$m' % das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm theo mẫu content
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

