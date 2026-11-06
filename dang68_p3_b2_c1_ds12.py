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


def bt_dang68_p3_b2_c1_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)

    if dang=='1':
        # Random kích thước tờ giấy
        # b là chiều rộng, a là chiều dài
        b = random.choice([8, 9, 10, 12, 14, 16])
        a_offset = random.choice([6, 8, 9, 10, 12])
        a = b + a_offset 

        # Tính toán kết quả chính xác theo công thức L_min = 3*b*sqrt(3)/4
        b_sp = Integer(b)
        L_exact_sympy = (3 * b_sp * sqrt(3)) / 4
        L_float = float((3 * b * math.sqrt(3)) / 4)

        # Làm tròn đến hàng phần chục theo yêu cầu đề bài
        kq3 = Decimal(str(L_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq = str(kq3).replace('.', ',')

        # Các đáp án trắc nghiệm
        du = ['$%s$'%(kq)]
        da = random.choice(du)

        # Tạo các phương án nhiễu (sai số nhỏ hoặc bẫy công thức)
        L_err1 = float(b * math.sqrt(2))
        L_err2 = float(4 * b / 3)
        L_err3 = float(L_float + 0.5)
        L_err4 = float(L_float - 0.5)
        L_err5 = float(L_float + 1.2)
        L_err6 = float(L_float - 1.2)

        err_list = [L_err1, L_err2, L_err3, L_err4, L_err5, L_err6]
        s = []
        for val in err_list:
            val_dec = Decimal(str(val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
            val_str = '$%s$' % str(val_dec).replace('.', ',')
            if val_str not in s and val_str != da:
                s.append(val_str)

        # Đảm bảo đủ 3 phương án sai
        random.shuffle(s)
        das1 = s[0]
        das2 = s[1]
        das3 = s[2]

        # Câu hỏi (Bao gồm cả code vẽ TikZ)
        noidungcauhoi = ('''\\immini{Một mảnh giấy hình chữ nhật có chiều dài $%s$ cm và chiều rộng $%s$ cm. Thực hiện thao tác gấp góc dưới bên phải sao cho đỉnh được gấp nằm trên cạnh chiều dài còn lại (như hình vẽ). Hỏi chiều dài $L$ tối thiểu của nếp gấp là bao nhiêu cm? (kết quả làm tròn đến hàng phần chục).}
    {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (53,32.27) -- (176.4,32.27) -- (176.4,202) -- (53,202) -- cycle ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,44.6) -- (68.67,193) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,44.6) -- (175.73,44.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,192.67) -- (175.73,192.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,118.47) -- (175.73,118.47) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,78.27) -- (175.73,78.27) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,157.93) -- (175.73,157.93) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,60.6) -- (175.73,60.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,98.27) -- (175.73,98.27) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (69.33,138.27) -- (176.4,138.27) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.33,175.93) -- (175.4,175.93) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,52.6) -- (175.73,52.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (69,69.6) -- (176.07,69.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (69,87.6) -- (176.07,87.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.33,107.93) -- (175.4,107.93) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,127.6) -- (175.73,127.6) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.67,147.93) -- (175.73,147.93) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (69,166.93) -- (176.07,166.93) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.33,184.6) -- (175.4,184.6) ;
    	\\draw  [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (176.4,80.67) -- (96.73,201.67) -- (53.4,125.2) -- cycle ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (176.4,80.67) -- (96.73,201.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (176.4,80.67) -- (176.4,202) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (176.4,202) -- (96.73,201.67) ;
    	\\draw  [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]  (60.4,123.2) -- (63.07,128.87) -- (56.4,131.2) -- (53.4,125.2) -- cycle ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.4,133.33) -- (167.4,94.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (68.4,133.33) -- (103.07,192.33) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (77.4,130.33) -- (112.07,189.33) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (86.07,127) -- (120.73,186) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (94.07,123.33) -- (128.73,182.33) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (102.07,120.67) -- (136.73,179.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (109.73,117.33) -- (144.4,176.33) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (117.9,114) -- (152.57,173) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (126.4,110.67) -- (161.07,169.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (134.73,107.33) -- (169.4,166.33) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (142.73,104.33) -- (157.4,129.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (150.4,101.67) -- (165.07,127) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (157.73,98.33) -- (172.4,123.67) ;
    	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ][line width=1]  (176.4,80.67) -- (176.4,202) -- (96.73,201.67) -- cycle ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]    (176.4,80.67) -- (96.73,201.67) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (176.4,80.67) -- (176.4,202) ;
    	\\draw [color={rgb, 255:red, 11; green, 115; blue, 92 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (96.73,201.67) -- (176.4,202) ;
    	\\draw  [color={rgb, 255:red, 11; green, 105; blue, 83 }  ,draw opacity=1 ][line width=1]  (53,32.27) -- (176.4,32.27) -- (176.4,80.67) -- (96.73,201.67) -- (53,202) -- cycle ;
    	\\draw (142.33,149.87) node [anchor=north west][inner sep=0.75pt]    {$L$};
    	\\draw (101,10) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%scm$};
    	\\draw (12.5,68) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$%scm$};
    	\\draw (38.33,199.37) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
    	\\draw (172.33,205) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
    	\\draw (88.83,205) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$E$};
    	\\draw (37.83,114.37) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$F$};
    	\\draw (178.33,65.87) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$G$};
    \\end{tikzpicture}}''' % (a, b, b, a))

        # Các đáp án
        da_d = ('\\True ' +str(da))
        da_s1 = str(das1)
        da_s2 = str(das2) 
        da_s3 = str(das3) 

        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_1 = [da_d,da_s1,da_s2,da_s3]
        random.shuffle(list_1)

        # Nội dung lời giải
        loigiai = ('''Đặt $EF = x = EB$, khi đó $AE = %s - x \\Rightarrow \\cos \\widehat{AEF} = \\frac{AE}{EF} = \\frac{%s - x}{x}$. \\\\
    Suy ra $\\cos(180^\\circ - \\widehat{FEB}) = \\frac{%s - x}{x} \\Leftrightarrow -\\cos \\widehat{FEB} = \\frac{%s - x}{x} \\Rightarrow \\cos \\widehat{FEB} = \\frac{x - %s}{x}$. \\\\
    Hay $\\cos(2 \\cdot \\widehat{GEB}) = \\frac{x - %s}{x} \\Rightarrow 2\\cos^2 \\widehat{GEB} - 1 = \\frac{x - %s}{x} \\Rightarrow \\cos \\widehat{GEB} = \\sqrt{\\frac{2x - %s}{2x}}$ \\\\
    (do $\\widehat{GEB} < 90^\\circ \\Rightarrow \\cos \\widehat{GEB} > 0$ và $\\Delta GEB = \\Delta FEG \\Rightarrow \\widehat{BEG} = \\widehat{FEG}$). \\\\
    Suy ra $EG = \\frac{EF}{\\cos \\widehat{FEG}} = \\frac{x}{\\cos \\widehat{GEB}} = \\frac{x}{\\sqrt{\\frac{2x - %s}{2x}}} = f(x)$. \\\\
    Ta có $f'(x) = \\frac{4x - %s}{(2x - %s)\\sqrt{4 - \\frac{%s}{x}}} = 0 \\Leftrightarrow x = \\frac{%s}{4} = %s$. \\\\
    Lập bảng biến thiên, ta thấy $EG$ nhỏ nhất khi $x = %s$.
    \\begin{center}
    \\begin{tikzpicture}
    \\tkzTabInit[lgt=1.5,espcl=3]
    {$x$ / 1, $f'(x)$ / 1, $f(x)$ / 2.5}
    {$\\frac{%s}{2}$, $\\frac{%s}{4}$, $+\\infty$}
    \\tkzTabLine{ d, -, 0, +, }
    \\tkzTabVar{ D+/ $+\\infty$ , -/ $%s$ , +/ $+\\infty$ }
    \\end{tikzpicture}
    \\end{center}
    Vậy chiều dài $L$ tối thiểu bằng $\\frac{x}{\\sqrt{\\frac{2x - %s}{2x}}} = %s \\approx %s$ cm.''' % (
            b, b, b, b, b, b, b, b, b, 3*b, b, 2*b, 3*b, str(3*b/4).replace('.', ','), str(3*b/4).replace('.', ','),
            b, 3*b, latex(L_exact_sympy), b, latex(L_exact_sympy), kq
        ))

    dapan='\\shortans[0]{$%s$}\n'%(kq)
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
        '\\loigiai{\n'+str(loigiai)+'\n}\n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

