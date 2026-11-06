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


def bt_dang75_p4_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo các danh sách biến ngẫu nhiên
            lis_k = [2, 3, 4, 5] # Các mẫu số của tỉ số (1/2, 1/3,...)
            k = random.choice(lis_k)
            k_plus_1 = k + 1

            # Các nhãn đỉnh (có thể random tên đỉnh nếu muốn, ở đây giữ nguyên theo hình)
            cube = "ABCD.A'B'C'D'"

            # --- B3: Suy nghĩ tìm cách random bài toán ---
            # Random tỉ số chia đoạn: BM = 1/k MA' và CN = 1/k NB'
            # Khi đó: (k+1)MN = k.BC + A'B' (Dựa trên logic phân tích vector trong ảnh)

            # Câu hỏi
            noidungcauhoi = (r"Cho hình lập phương $%s$. Gọi $M, N$ lần lượt là các điểm thuộc $A'B$ và $B'C$ "
                             r"sao cho $\vec{BM} = \frac{1}{%s} \vec{MA'}$; $\vec{CN} = \frac{1}{%s} \vec{NB'}$. "
                             r"Tính tích vô hướng $k \cdot \vec{MN} \cdot \vec{A'B}$ (với $k = %s$ và cạnh hình lập phương bằng $a$)."
                             % (cube, latex(k), latex(k), latex(k_plus_1)))

            # Đáp án (Dựa trên kết quả A'B'.A'B = a^2)
            da_dung = r'$a^2$'
            s = [r'$0$', r'$2a^2$', r'$-a^2$', r'$\frac{1}{2}a^2$', r'$3a^2$', r'$-2a^2$']

            # Chọn ngẫu nhiên các đáp án sai
            list_s = random.sample(s, 3)
            da_s1, da_s2, da_s3 = list_s[0], list_s[1], list_s[2]

            # Nội dung lời giải (Viết lại y hệt logic trong ảnh nhưng dùng biến k)
            loigiai = ('\\begin{center}'
                       '''\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=0.8cm,y=0.8cm]
            	\\clip(-1.2,-0.6) rectangle (6.3,4.6);
            	\\draw (0.,0.)-- (0.,3.);
            	\\draw (0.,0.)-- (4.,0.);
            	\\draw (4.,0.)-- (4.,3.);
            	\\draw (0.,3.)-- (4.,3.);
            	\\draw (0.,3.)-- (2.,4.);
            	\\draw (2.,4.)-- (5.,4.);
            	\\draw (5.,4.)-- (4.,3.);
            	\\draw (5.,4.)-- (5.,1.);
            	\\draw (5.,1.)-- (4.,0.);
            	\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (2.,1.);
            	\\draw [dash pattern=on 1pt off 1pt] (2.,1.)-- (2.,4.);
            	\\draw [dash pattern=on 1pt off 1pt] (2.,1.)-- (5.,1.);
            	\\draw (4.,0.)-- (0.,3.);
            	\\draw (5.,1.)-- (4.,3.);
            	\\path (0:0) coordinate (S) 
            	($(4,3)!1/%s!(5,1)$) coordinate ({M})
            	($(0,3)!1/%s!(4,0)$) coordinate ({N});
            	\\foreach \\x/\\g in {M/45,N/220} 
            	\\draw[fill=black] (\\x) circle (0.00005) node[shift={(\\g:.3)}]{$\\x$};
            	\\draw [densely dashed] (M)--(N);
            	\\draw (5,4.46) node[anchor=north west] {$A$};
            	\\draw (3.6,3.6) node[anchor=north west] {$B$};
            	\\draw (-0.55,3.5) node[anchor=north west] {$C$};
            	\\draw (1.5,4.56) node[anchor=north west] {$D$};
            	\\draw (5,1.26) node[anchor=north west] {$A'$};
            	\\draw (4,0.2) node[anchor=north west] {$B'$};
            	\\draw (-0.3,0) node[anchor=north west] {$C'$};
            	\\draw (1.830,1) node[anchor=north west] {$D'$};
            \\end{tikzpicture}'''
                '\\end{center}'
                r"Ta có: $\begin{cases} \vec{MN} = \vec{MB} + \vec{BC} + \vec{CN} \Rightarrow %s\vec{MN} = %s\vec{MB} + %s\vec{BC} + %s\vec{CN} \\ \vec{MN} = \vec{MA'} + \vec{A'B'} + \vec{B'C} \end{cases}$ \\ "
                       r"Cộng hai vế và sử dụng giả thiết $%s\vec{MB} + \vec{MA'} = \vec{0}$ và $%s\vec{CN} + \vec{B'C} = \vec{0}$ (theo tỉ số đề bài), ta được: \\ "
                       r"$\Rightarrow %s\vec{MN} = %s\vec{BC} + \vec{A'B'}$. \\ "
                       r"Xét tích vô hướng: \\ "
                       r"$%s\vec{MN} \cdot \vec{A'B} = (%s\vec{BC} + \vec{A'B'}) \cdot \vec{A'B} = %s\vec{BC} \cdot \vec{A'B} + \vec{A'B'} \cdot \vec{A'B}$. \\ "
                       r"Vì $\vec{BC} \perp \vec{A'B}$ nên $\vec{BC} \cdot \vec{A'B} = 0$. \\ "
                       r"$\Rightarrow %s\vec{MN} \cdot \vec{A'B} = \vec{A'B'} \cdot (\vec{A'B'} + \vec{B'B}) = \vec{A'B'}^2 = a^2$."
                       % (latex(k_plus_1),
                           latex(k_plus_1),

                          latex(k), latex(k), latex(k), latex(k), 
                          latex(k), latex(k), 
                          latex(k_plus_1), latex(k), 
                          latex(k_plus_1), latex(k), latex(k),
                          latex(k_plus_1)))

            # Trộn đáp án
            list_1 = ['\\True ' + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất kết quả theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

