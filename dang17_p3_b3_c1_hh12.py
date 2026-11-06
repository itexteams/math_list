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


def bt_dang17_p3_b3_c1_hh12(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)

    if dang == '1':

        r1 = 2
        r2 = 3
        AB_val = 2 * r1


        # Random các giá trị x_C, y_C đẹp để tạo các bộ AC, BC khác nhau:
        x_C = choice([8, 10, 12])
        y_C = choice([-24, -22, -20, -18])
        v_val = choice([2, 3])

        AC2 = x_C**2 + (y_C - 2)**2
        BC2 = x_C**2 + (y_C + 2)**2

        # Biểu diễn AC và BC dưới dạng căn rút gọn hoặc số nguyên
        AC_sym = sqrt(AC2)
        BC_sym = sqrt(BC2)


        const_part = x_C**2 + y_C**2 + 20
        coeff_sqrt5 = 4 * x_C

        CC_prime_val = math.sqrt(const_part - coeff_sqrt5 * math.sqrt(5))
        t_val = CC_prime_val / v_val

        # Làm tròn đến hàng phần mười
        number = Decimal(str(t_val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Hình vẽ TikZ
        hinhve = '''\\begin{center}
        	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
        		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (80.33,70) .. controls (80.33,56.19) and (91.53,45) .. (105.33,45) .. controls (119.14,45) and (130.33,56.19) .. (130.33,70) .. controls (130.33,83.81) and (119.14,95) .. (105.33,95) .. controls (91.53,95) and (80.33,83.81) .. (80.33,70) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (83.87,66.73) .. controls (83.87,56.76) and (91.96,48.67) .. (101.93,48.67) .. controls (111.91,48.67) and (120,56.76) .. (120,66.73) .. controls (120,76.71) and (111.91,84.8) .. (101.93,84.8) .. controls (91.96,84.8) and (83.87,76.71) .. (83.87,66.73) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (89.93,61.37) .. controls (89.93,57.67) and (92.93,54.67) .. (96.63,54.67) .. controls (100.33,54.67) and (103.33,57.67) .. (103.33,61.37) .. controls (103.33,65.07) and (100.33,68.07) .. (96.63,68.07) .. controls (92.93,68.07) and (89.93,65.07) .. (89.93,61.37) -- cycle ;
        		\\draw  [fill={rgb, 255:red, 74; green, 144; blue, 226 }  ,fill opacity=1 ] (79.67,121) .. controls (79.67,107.19) and (90.86,96) .. (104.67,96) .. controls (118.47,96) and (129.67,107.19) .. (129.67,121) .. controls (129.67,134.81) and (118.47,146) .. (104.67,146) .. controls (90.86,146) and (79.67,134.81) .. (79.67,121) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (83.2,117.73) .. controls (83.2,107.76) and (91.29,99.67) .. (101.27,99.67) .. controls (111.24,99.67) and (119.33,107.76) .. (119.33,117.73) .. controls (119.33,127.71) and (111.24,135.8) .. (101.27,135.8) .. controls (91.29,135.8) and (83.2,127.71) .. (83.2,117.73) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (89.27,112.37) .. controls (89.27,108.67) and (92.27,105.67) .. (95.97,105.67) .. controls (99.67,105.67) and (102.67,108.67) .. (102.67,112.37) .. controls (102.67,116.07) and (99.67,119.07) .. (95.97,119.07) .. controls (92.27,119.07) and (89.27,116.07) .. (89.27,112.37) -- cycle ;
        		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (266.33,171.03) .. controls (266.33,150.76) and (282.76,134.33) .. (303.03,134.33) .. controls (323.3,134.33) and (339.73,150.76) .. (339.73,171.03) .. controls (339.73,191.3) and (323.3,207.73) .. (303.03,207.73) .. controls (282.76,207.73) and (266.33,191.3) .. (266.33,171.03) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=0.5 ] (271.52,166.24) .. controls (271.52,151.59) and (283.39,139.72) .. (298.04,139.72) .. controls (312.69,139.72) and (324.56,151.59) .. (324.56,166.24) .. controls (324.56,180.89) and (312.69,192.76) .. (298.04,192.76) .. controls (283.39,192.76) and (271.52,180.89) .. (271.52,166.24) -- cycle ;
        		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (280.43,158.36) .. controls (280.43,152.93) and (284.83,148.52) .. (290.26,148.52) .. controls (295.69,148.52) and (300.1,152.93) .. (300.1,158.36) .. controls (300.1,163.79) and (295.69,168.2) .. (290.26,168.2) .. controls (284.83,168.2) and (280.43,163.79) .. (280.43,158.36) -- cycle ;
        		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (104.67,121) -- (303.03,171.03) ;
        		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (105.33,70) -- (303.03,171.03) ;
        		\\draw  [dash pattern={on 4.5pt off 4.5pt}]  (105.33,70) -- (104.67,121) ;
        		\\draw (86.67,60.33) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$A$};
        		\\draw (89.33,117) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$B$};
        		\\draw (298.04,173) node [anchor=north west][inner sep=0.75pt]  [font=\\footnotesize]  {$C$};
        	\\end{tikzpicture}
        \\end{center}'''

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên một mặt sàn phẳng, có hai viên bi màu xanh đứng yên và tiếp xúc nhau. Gọi $A, B$ lần lượt là các điểm tiếp xúc của hai viên bi xanh với mặt sàn; mỗi viên bi xanh có bán kính $%s\\text{ cm}$. Một viên bi màu vàng có bán kính $%s\\text{ cm}$, ban đầu tiếp xúc với mặt sàn tại điểm $C$, trong đó $AC = %s\\text{ cm}$, $BC = %s\\text{ cm}$. Viên bi vàng lăn thẳng đều trên mặt sàn về phía hai viên bi xanh với tốc độ $%s\\text{ cm/s}$. Hỏi sau bao nhiêu giây kể từ lúc xuất phát thì viên bi vàng tiếp xúc cùng lúc với hai viên bi xanh? (Làm tròn kết quả đến hàng phần mười). %s'''
                         % (str(r1), str(r2), latex(AC_sym), latex(BC_sym), str(v_val), hinhve))



        # Nội dung lời giải
        loigiai = ('''Gọi $I_1, I_2$ lần lượt là tâm của hai viên bi xanh và $I_3$ là tâm của viên bi vàng. \\\\
                   Vì hai viên bi xanh có bán kính $r_1 = %s\\text{ cm}$, tiếp xúc ngoài với nhau và cùng tiếp xúc mặt sàn tại $A, B$ nên: \\\\
                   $AB = I_1I_2 = r_1 + r_1 = %s\\text{ cm}$. \\\\
                   Tâm $I_1, I_2$ có độ cao so với mặt sàn là $z_1 = z_2 = %s\\text{ cm}$, còn tâm viên bi vàng có độ cao $z_3 = r_2 = %s\\text{ cm}$. \\\\
                   Chọn hệ trục tọa độ $Oxy$ trên mặt sàn sao cho gốc $O$ là trung điểm của $AB$, trục $Oy$ chứa đường thẳng $AB$ (chiều dương từ $B$ đến $A$). \\\\
                   Khi đó tọa độ các điểm là $A(0; 2)$ và $B(0; -2)$. \\\\
                   Gọi $C(x; y)$ với $x > 0$. Theo đề bài: \\\\
                   $\\begin{cases} AC^2 = x^2 + (y - 2)^2 = %s \\\\ BC^2 = x^2 + (y + 2)^2 = %s \\end{cases}$ \\\\
                   Trừ hai phương trình vế theo vế, ta được: \\\\
                   $(y - 2)^2 - (y + 2)^2 = %s - %s \\Leftrightarrow -8y = %s \\Leftrightarrow y = %s$. \\\\
                   Thay $y = %s$ vào phương trình thứ nhất: \\\\
                   $x^2 + (%s - 2)^2 = %s \\Leftrightarrow x^2 = %s \\Rightarrow x = %s$ (do $x > 0$). \\\\
                   Vậy tọa độ ban đầu của điểm $C$ là $C(%s; %s)$. \\\\
                   Khi viên bi vàng lăn đến vị trí tiếp xúc cùng lúc với hai viên bi xanh, gọi $C'$ là vị trí tiếp xúc mới của viên bi vàng với mặt sàn và $I_3'$ là tâm của viên bi vàng lúc đó. \\\\
                   Khoảng cách giữa tâm viên bi vàng và tâm mỗi viên bi xanh là $I_1I_3' = I_2I_3' = r_1 + r_2 = %s + %s = 5\\text{ cm}$. \\\\
                   Chênh lệch độ cao giữa hai tâm là $\\Delta z = z_3 - z_1 = %s - %s = 1\\text{ cm}$. \\\\
                   Hình chiếu khoảng cách lên mặt phẳng sàn là: \\\\
                   $C'A^2 = C'B^2 = (I_1I_3')^2 - (\\Delta z)^2 = 5^2 - 1^2 = 24\\text{ cm}^2$. \\\\
                   Do $C'A = C'B$ nên $C'$ thuộc đường trung trực của đoạn thẳng $AB$ (chính là trục hoành $Ox$), tức là $y_{C'} = 0$. \\\\
                   Tam giác $C'AB$ cân tại $C'$ có trung tuyến $C'O$, do đó: \\\\
                   $C'O^2 = C'A^2 - OA^2 = 24 - 2^2 = 20 \\Rightarrow x_{C'} = \\sqrt{20} = 2\\sqrt{5}$ (do viên bi lăn về phía hai viên bi xanh từ miền $x > 0$). \\\\
                   Suy ra tọa độ điểm tiếp xúc lúc đó là $C'(2\\sqrt{5}; 0)$. \\\\
                   Quãng đường viên bi vàng lăn thẳng trên mặt sàn là độ dài đoạn thẳng $CC'$: \\\\
                   $CC' = \\sqrt{(x_{C'} - x_C)^2 + (y_{C'} - y_C)^2} = \\sqrt{(2\\sqrt{5} - %s)^2 + (0 - (%s))^2} = \\sqrt{%s - %s\\sqrt{5}} \\approx %s\\text{ cm}$. \\\\
                   Thời gian để viên bi vàng lăn đến vị trí tiếp xúc là: \\\\
                   $t = \\dfrac{CC'}{v} \\approx \\dfrac{%s}{%s} \\approx %s\\text{ (giây)}$.'''
                   % (str(r1),
                      str(AB_val),
                      str(r1), str(r2),
                      str(AC2), str(BC2),
                      str(AC2), str(BC2), str(AC2 - BC2), str(y_C),
                      str(y_C),
                      str(y_C), str(AC2), str(x_C**2), str(x_C),
                      str(x_C), str(y_C),
                      str(r1), str(r2),
                      str(r2), str(r1),
                      str(x_C), str(y_C), str(const_part), str(coeff_sqrt5), str(Decimal(str(CC_prime_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','),
                      str(Decimal(str(CC_prime_val)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','), str(v_val), str(kq_str)
                   ))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' + '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) + '\\loigiai{ \n' + str(loigiai) + '}\n' + '\\end{ex}\n \\end{minipage} \n\n')
    return content

