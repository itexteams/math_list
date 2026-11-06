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


def bt_dang51_p3_b3_c3_ds12(self):
            # --- BƯỚC 1: CHỌN THÔNG SỐ NGẪU NHIÊN ---
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random cấu hình bài toán: (xp, xq, m_delta)
                # Các cấu hình đã được tính toán lại để đảm bảo B - A luôn là số nguyên
                configs = [
                    (2, 1, -1), # P(2,8), Q(1,4), Delta: y = -x + 5. Kết quả: 6
                    (2, 1, -2), # P(2,8), Q(1,4), Delta: y = -2x + 6. Kết quả: 2
                    (4, 2, -8), # P(4,64), Q(2,32), Delta: y = -8x + 48. Kết quả: 32
                    (4, 1, -2)  # P(4,64), Q(1,16), Delta: y = -2x + 18. Kết quả: 8
                ]
                xp, xq, m_delta = random.choice(configs)

                # Tính toán các thông số phái sinh
                yp = xp**3
                md = Rational(yp, xp) # Hệ số góc đường thẳng d: y = md * x
                yq = md * xq
                c = yq - m_delta * xq
                xr = Rational(-c, m_delta)
                xr_float = float(xr)

                # Hàm số
                fx = x**3
                dx_line = md * x
                deltax = m_delta * x + c

                if m_delta == -1:
                    str_delta = "-x + %s" % (c)
                else:
                    str_delta = "%sx + %s" % (m_delta, c)

                # Tính x_S (giao điểm của curve và delta) bằng nsolve để vẽ TikZ chính xác
                try:
                    xs_val = float(nsolve(fx - deltax, x, (xq + xp)/2.0))
                except:
                    xs_val = (xq + xp) / 2.0

                # Tính tích phân
                I1 = integrate(fx, (x, 0, xp))
                I2 = integrate(deltax, (x, xq, xr))
                I3 = integrate(dx_line, (x, xq, xp))

                # Kết quả B - A
                kq = I1 + I2 - I3

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (latex(kq).replace('.', ','))]
                da = du[0]

                # Tạo các phương án sai (distractors)
                s = [
                    '$%s$' % (latex(kq + 1)).replace('.', ','),
                    '$%s$' % (latex(kq - 1)).replace('.', ','),
                    '$%s$' % (latex(kq + Rational(1,2))).replace('.', ','),
                    '$%s$' % (latex(kq - Rational(1,2))).replace('.', ','),
                    '$%s$' % (latex(kq + 2)).replace('.', ','),
                    '$%s$' % (latex(kq - 2)).replace('.', ','),
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                hinhve=r'''\scalebox{0.7}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (199.2,149.76) .. controls (254,178.96) and (282.4,192.16) .. (322.4,214.56) .. controls (315.6,211.76) and (163.6,214.16) .. (121.53,213.67) .. controls (171.6,208.96) and (189.6,172.56) .. (199.2,149.76) -- cycle ;
            	\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (222.4,62.56) .. controls (213.2,128.96) and (203.2,139.36) .. (199.2,149.76) .. controls (192.4,146.96) and (183.6,140.56) .. (173.2,135.36) .. controls (191.2,110.92) and (201.6,92.16) .. (222.4,62.56) -- cycle ;
            	\draw [line width=1]    (104.67,214) -- (369.07,214.13) ;
            	\draw [shift={(373.07,214.13)}, rotate = 180.03] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            	\draw [line width=1]    (122.4,234.8) -- (121.75,16.8) ;
            	\draw [shift={(121.73,12.8)}, rotate = 89.83] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
            	\draw [line width=1]    (121.53,213.67) -- (240.4,34.8) ;
            	\draw [line width=1]    (100.4,97.47) -- (365.73,236.8) ;
            	\draw [line width=1]    (121.53,213.67) .. controls (186.4,210.8) and (219.07,134.13) .. (224.4,28.13) ;
            	\draw (99,219) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (353.6,195) node [anchor=north west][inner sep=0.75pt]    {$x$};
            	\draw (101.6,15) node [anchor=north west][inner sep=0.75pt]    {$y$};
            	\draw (183.2,122) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (208,178.6) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (158.4,108.2) node [anchor=north west][inner sep=0.75pt]    {$Q$};
            	\draw (201.6,49) node [anchor=north west][inner sep=0.75pt]    {$P$};
            	\draw (240.4,34.8) node [anchor=north west][inner sep=0.75pt]    {$d$};
            	\draw (167.2,18.6) node [anchor=north west][inner sep=0.75pt]    {$y=x^{3}$};
            	\draw (318.4,218.6) node [anchor=north west][inner sep=0.75pt]    {$\Delta $};
            \end{tikzpicture} }'''   
                # Câu hỏi
                # Ghi chú: Đã xóa phần "làm tròn kết quả..." khỏi câu hỏi
                noidungcauhoi = (r'''\immini{Cho hàm số $f(x) = x^3$. Đường thẳng $d$ đi qua gốc tọa độ $O$ và điểm $P(%s; f(%s))$ cắt đường thẳng $\Delta : y = %s$ tại điểm $Q$. Gọi $R$ là giao điểm của đường thẳng $\Delta$ với trục hoành. Gọi $A$ là diện tích hình phẳng giới hạn bởi đường cong $y = f(x)$, đường thẳng $\Delta$ và đoạn thẳng $PQ$; $B$ là diện tích hình phẳng giới hạn bởi đường cong $y = f(x)$, đường thẳng $\Delta$ và trục hoành. Giá trị của $B - A$ bằng bao nhiêu?}{%s}''' % (
                    xp, xp, str_delta,hinhve
                ))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $x_1$ là hoành độ giao điểm của đường cong $y=f(x)$ và đường thẳng $\\Delta$.
            Từ đồ thị ta thấy:
            \\begin{itemize}
                \\item Diện tích $A = \\int_{%s}^{x_1} \\left( d(x) - \\Delta(x) \\right) \\mathrm{d}x + \\int_{x_1}^{%s} \\left( d(x) - f(x) \\right) \\mathrm{d}x$ \\\\
                $\\Rightarrow A = \\int_{%s}^{%s} d(x) \\mathrm{d}x - \\int_{%s}^{x_1} \\Delta(x) \\mathrm{d}x - \\int_{x_1}^{%s} f(x) \\mathrm{d}x$.
                \\item Diện tích $B = \\int_{0}^{x_1} f(x) \\mathrm{d}x + \\int_{x_1}^{%s} \\Delta(x) \\mathrm{d}x$.
            \\end{itemize}
            Khi đó:
            \\begin{align*}
            B - A &= \\left( \\int_{0}^{x_1} f(x) \\mathrm{d}x + \\int_{x_1}^{%s} \\Delta(x) \\mathrm{d}x \\right) - \\left( \\int_{%s}^{%s} d(x) \\mathrm{d}x - \\int_{%s}^{x_1} \\Delta(x) \\mathrm{d}x - \\int_{x_1}^{%s} f(x) \\mathrm{d}x \\right) \\\\
            &= \\left( \\int_{0}^{x_1} f(x) \\mathrm{d}x + \\int_{x_1}^{%s} f(x) \\mathrm{d}x \\right) + \\left( \\int_{%s}^{x_1} \\Delta(x) \\mathrm{d}x + \\int_{x_1}^{%s} \\Delta(x) \\mathrm{d}x \\right) - \\int_{%s}^{%s} d(x) \\mathrm{d}x \\\\
            &= \\int_{0}^{%s} f(x) \\mathrm{d}x + \\int_{%s}^{%s} \\Delta(x) \\mathrm{d}x - \\int_{%s}^{%s} d(x) \\mathrm{d}x.
            \\end{align*}
            Ta có đường thẳng $d$ đi qua $O(0;0)$ và $P(%s; %s)$ nên có phương trình $y = %sx$.
            Tọa độ điểm $Q$ là giao điểm của $d$ và $\\Delta$: $Q(%s; %s)$.
            Tọa độ điểm $R$ là giao điểm của $\\Delta$ và trục hoành: $R\\left(%s; 0\\right)$.
            Thế vào biểu thức trên, ta được:
            \\begin{align*}
            B - A &= \\int_{0}^{%s} x^3 \\mathrm{d}x + \\int_{%s}^{%s} \\left(%s\\right) \\mathrm{d}x - \\int_{%s}^{%s} %sx \\mathrm{d}x \\\\
            &= \\left. \\frac{x^4}{4} \\right|_{0}^{%s} + \\left. \\left( %s \\right) \\right|_{%s}^{%s} - \\left. \\left( %s \\right) \\right|_{%s}^{%s} \\\\
            &= %s + %s - %s = %s.
            \\end{align*}''' % (
                    xq, xp, xq, xp, xq, xp, latex(xr),
                    latex(xr), xq, xp, xq, xp,
                    xp, xq, latex(xr), xq, xp,
                    xp, xq, latex(xr), xq, xp,
                    xp, yp, md,
                    xq, yq,
                    latex(xr),
                    xp, xq, latex(xr), str_delta, xq, xp, md,
                    xp, latex(integrate(deltax, x)), xq, latex(xr), latex(integrate(dx_line, x)), xq, xp,
                    latex(I1), latex(I2), latex(I3), latex(kq).replace('.', ',')
                ))
                dapan='\\shortans[0]{$%s$}\n'%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

