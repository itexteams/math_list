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


def bt_dang14_p3_b5_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random độ dài cạnh đáy và chiều cao
                a = random.randint(2, 6) * 2  # Cạnh đáy BA = BC
                h = random.randint(3, 9)      # Chiều cao AA'

                # Tính toán kết quả chính xác
                # 1/BK^2 = 1/h^2 + 1/a^2 => BK^2 = (a^2 * h^2) / (a^2 + h^2)
                tu_bk2 = a**2 * h**2
                mau_bk2 = a**2 + h**2
                g = math.gcd(tu_bk2, mau_bk2)
                tu_simp = tu_bk2 // g
                mau_simp = mau_bk2 // g

                bk_val = math.sqrt(tu_bk2 / mau_bk2)
                kq3 = Decimal(float(bk_val)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq = str(kq3).replace('.', ',')

                # Định dạng chuỗi LaTeX cho phân số của BK^2
                if mau_simp == 1:
                    bk2_latex = f"{tu_simp}"
                else:
                    bk2_latex = f"\\frac{{{tu_simp}}}{{{mau_simp}}}"

                # Định dạng chuỗi LaTeX cho giá trị chính xác của BK
                if math.isqrt(tu_simp)**2 == tu_simp:
                    if mau_simp == 1:
                        bk_latex = f"{math.isqrt(tu_simp)}"
                    else:
                        bk_latex = f"\\frac{{{math.isqrt(tu_simp)}}}{{\\sqrt{{{mau_simp}}}}}"
                else:
                    if mau_simp == 1:
                        bk_latex = f"\\sqrt{{{tu_simp}}}"
                    else:
                        bk_latex = f"\\sqrt{{\\frac{{{tu_simp}}}{{{mau_simp}}}}}"

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq)]
                da = random.choice(du)

                # Sinh các phương án sai ngẫu nhiên (không trùng lặp)
                s_set = set()
                offsets = [0.1, -0.1, 0.2, -0.2, 0.3, -0.3, 1.0, -1.0]
                for off in offsets:
                    dist_val = Decimal(float(bk_val + off)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    if dist_val > 0:
                        s_set.add('$%s$' % str(dist_val).replace('.', ','))

                if da in s_set:
                    s_set.remove(da)

                s = list(s_set)
                random.shuffle(s)

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lăng trụ đứng $ABC.A'B'C'$ có đáy là tam giác vuông cân tại đỉnh $B$. Biết rằng cạnh đáy $BA = BC = %s$ cm và chiều cao của lăng trụ $AA' = %s$ cm. Hãy tính khoảng cách giữa hai đường thẳng $A'C$ và $AB$ (Kết quả làm tròn đến hàng phần chục).''' 
                                 % (latex(a), latex(h)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Mã lệnh vẽ hình bằng TikZ
                tikz_code = '''\\begin{center}
                \\begin{tikzpicture}[scale=0.8, line width=1pt]
                    \\coordinate (A) at (0,3);
                    \\coordinate (B) at (-1.5,1.5);
                    \\coordinate (C) at (3.5,1.5);
                    \\coordinate (D) at (5,3);
                    \\coordinate (A1) at (0,0);
                    \\coordinate (B1) at (-1.5,-1.5);
                    \\coordinate (C1) at (3.5,-1.5);
                    \\coordinate (D1) at (5,0);
                    \\coordinate (K) at (0.35,-0.3);
                    \\draw (A) node[above]{$A$} -- (B) node[left]{$B$} -- (C) node[right]{$C$} -- (D) node[right]{$D$} -- cycle;
                    \\draw (B) -- (B1) node[left]{$B'$};
                    \\draw (C) -- (C1) node[right]{$C'$};
                    \\draw (D) -- (D1) node[right]{$D'$};
                    \\draw (B1) -- (C1) -- (D1);
                    \\draw (A) -- (C);
                    \\draw (B1) -- (C);
                    \\draw[dashed] (A) -- (A1) node[left]{$A'$};
                    \\draw[dashed] (A1) -- (B1);
                    \\draw[dashed] (A1) -- (D1);
                    \\draw[dashed] (A1) -- (C);
                    \\draw[dashed] (B) -- (K) node[below]{$K$};
                    \\draw[dashed] (A1) -- (K);
                \\end{tikzpicture}
                \\end{center}'''

                # Nội dung lời giải
                loigiai = ('''\\textbf{Phương pháp:} Dựng một mặt phẳng chứa đường thẳng này và song song với đường thẳng kia. Sau đó quy về bài toán khoảng cách từ một điểm đến một mặt phẳng. Có thể tính thông qua khối lăng trụ.\\\\
                %s
                Khi đó: $d(A'C; AB) = d(AB; (A'B'C)) = d(A; (A'B'C)) = d(B; (A'B'C))$\\\\
                Kẻ $BK \\perp B'C \\Rightarrow d(B; (A'B'C)) = BK$. Xét tam giác vuông $B'BC$ tại $B$ ta có:\\\\
                $\\frac{1}{BK^2} = \\frac{1}{BB'^2} + \\frac{1}{BC^2} \\Rightarrow BK^2 = %s \\Rightarrow BK = %s = %s... \\approx %s$ (cm)'''
                           % (tikz_code, bk2_latex, bk_latex, str(bk_val)[:5].replace('.', ','), kq))
                dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
                       '\\loigiai{\n'+str(loigiai)+'\n}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

