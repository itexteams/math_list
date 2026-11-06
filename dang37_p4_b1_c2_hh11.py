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


def bt_dang37_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Ở đây k=2 tương ứng với trung điểm như đề bài gốc
            lis_k = [2, 3, 4]
            k = random.choice(lis_k)

            # Tính toán các cạnh của tam giác B'NC dựa trên tỉ lệ k
            # Giả sử cạnh hình lập phương là a
            # B'N song song với C'M. N nằm trên AA' sao cho AN = DM = a/k => A'N = a(1 - 1/k)
            # Tọa độ hóa: D(0,0,0), A(a,0,0), C(0,a,0), D'(0,0,a)
            # B'(a,a,a), C(0,a,0), M(0,0, a/k) -> Vector CB' = (a,0,a), Vector MC' = (0,a, a - a/k)
            # cos = |a^2(1 - 1/k)| / (sqrt(2)a * sqrt(a^2 + a^2(1-1/k)^2))

            a = symbols('a')
            dm_ratio = Rational(1, k)
            # Tính độ dài các cạnh theo a
            # B'N^2 = A'B'^2 + A'N^2 = a^2 + (a(1-1/k))^2
            bn_sq = a**2 + (a*(1 - dm_ratio))**2
            bn = simplify(sqrt(bn_sq))

            # B'C^2 = a^2 + a^2 = 2a^2
            bc_sq = 2*a**2
            bc = simplify(sqrt(bc_sq))

            # NC^2 = ND^2 + DC^2 = (a/k)^2 + a^2 + a^2 (Tính khoảng cách N(a,0,a/k) đến C(0,a,0))
            nc_sq = a**2 + a**2 + (a*dm_ratio)**2
            nc = simplify(sqrt(nc_sq))

            # Tính cosin theo định lý hàm số cos: cos = (B'N^2 + B'C^2 - NC^2) / (2 * B'N * B'C)
            tu_so = bn_sq + bc_sq - nc_sq
            mau_so = 2 * bn * bc
            cos_val = simplify(tu_so / mau_so)

            # Đáp án đúng
            da = '$%s$' % latex(cos_val)

            # Tạo các đáp án nhiễu
            s = [
                '$%s$' % latex(simplify(Rational(1, k+1) * sqrt(2))),
                '$%s$' % latex(simplify(Rational(1, k) * sqrt(3))),
                '$%s$' % latex(simplify(cos_val * Rational(2, 3))),
                '$%s$' % latex(simplify(sqrt(Rational(1, k**2 + 1)))),
                '$%s$' % latex(simplify(Rational(1, k))),
                '$%s$' % latex(simplify(sqrt(Rational(k, 10))))
            ]

            # Loại bỏ trùng lặp nếu có và lấy 3 đáp án sai
            s = list(set(s))
            if da in s: s.remove(da)
            random.shuffle(s)
            das1, das2, das3 = s[:3]

            # --- NỘI DUNG CÂU HỎI ---
            ratio_text = "trung điểm" if k == 2 else "điểm sao cho $DM = \\frac{1}{%d} DD'$" % k
            noidungcauhoi = (r'''Cho hình lập phương $ABCD.A'B'C'D'$. Gọi $M$ là %s của $DD'$. Tính cosin của góc giữa hai đường thẳng $B'C$ và $C'M$.'''
                             % ratio_text)

            # --- NỘI DUNG LỜI GIẢI ---
            # Tạo TikZ cho hình vẽ
            tikz_code = r'''\begin{center}
            \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]   (91.47,60.07) -- (221.47,61.07) ;
            	\draw [line width=1]   (62.47,103.07) -- (192.47,104.07) ;
            	\draw [line width=1]   (62.47,195.07) -- (192.47,196.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (91.47,161.07) -- (221.47,162.07) ; 
            	\draw [line width=1]   (62.47,103.07) -- (62.47,195.07) ;
            	\draw [line width=1]   (192.47,104.07) -- (192.47,196.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (91.47,60.07) -- (91.47,161.07) ;
            	\draw [line width=1]   (221.47,61.07) -- (221.47,162.07) ;
            	\draw [line width=1]   (62.47,103.07) -- (91.47,60.07) ;
            	\draw [line width=1]   (192.47,104.07) -- (221.47,61.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (62.47,195.07) -- (91.47,161.07) ;
            	\draw [line width=1]   (192.47,196.07) -- (221.47,162.07) ;
            	\draw [line width=1]   (192.47,196.07) -- (221.47,61.07) ;
            	\draw [line width=1]   (62.47,149.07) -- (192.47,104.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (91.47,161.07) -- (192.47,196.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (91.47,110.57) -- (221.47,61.07) ;
            	\draw [line width=1] [dash pattern={on 5.63pt off 4.5pt}]  (91.47,110.57) -- (192.47,196.07) ;
            	\draw (71,145) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (226,148) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (192.47,196.07) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (45,194) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (71,42) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            	\draw (222,45) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            	\draw (193,97) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            	\draw (38,93) node [anchor=north west][inner sep=0.75pt]    {$D'$};
            	\draw (72,101) node [anchor=north west][inner sep=0.75pt]    {$N$};
            \end{tikzpicture}
            \end{center}''' 

            loigiai = (r'''Gọi $N$ là điểm trên cạnh $AA'$ sao cho $AN = DM \Rightarrow B'N \parallel C'M$. \\
            Khi đó, góc giữa $(B'C, C'M) = (B'C, B'N) = \widehat{NB'C}$ (hoặc bù với góc này). \\
            Giả sử hình lập phương có cạnh bằng $a$. Xét tam giác $B'NC$: \\
            - $B'N = \sqrt{A'B'^2 + A'N^2} = \sqrt{a^2 + \left(%s\right)^2} = %s$. \\
            - $B'C = \sqrt{BC^2 + BB'^2} = \sqrt{a^2 + a^2} = %s$. \\
            - $NC = \sqrt{ND^2 + DC^2} = \sqrt{\left(AN^2+AD^2\right) + DC^2} = \sqrt{%s + a^2 + a^2} = %s$. \\
            Áp dụng định lý hàm số cosin trong tam giác $B'NC$: \\
            $\cos \widehat{NB'C} = \frac{B'N^2 + B'C^2 - NC^2}{2 \cdot B'N \cdot B'C} = \frac{%s + %s - %s}{2 \cdot %s \cdot %s} = %s$. \\
            Vậy cosin của góc cần tìm là $%s$.''' 
            % (latex(a*(1-dm_ratio)), latex(bn), latex(bc), latex((a*dm_ratio)**2), latex(nc),
               latex(bn_sq), latex(bc_sq), latex(nc_sq), latex(bn), latex(bc), latex(cos_val),
               latex(cos_val)))

            # --- XUẤT KẾT QUẢ ---
            list_1 = ['\\True ' + str(da), str(das1), str(das2), str(das3)]
            random.shuffle(list_1)

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n' 
                '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

