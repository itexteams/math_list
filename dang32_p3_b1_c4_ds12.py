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


def bt_dang32_p3_b1_c4_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Random tổng điểm để tạo ra các bài toán khác nhau (16 là bài gốc, 14 là bài tương tự)
                S = random.choice([14, 16])

                if S == 16:
                    kq_exact = "0,14"
                    s_list = ["0,15", "0,12", "0,21", "0,17", "0,20"]
                    loigiai_text = ('''Gọi $x_1, x_2, x_3, x_4, x_5, x_6$ lần lượt là điểm đánh giá của $6$ tiêu chí.\\\\
            Theo đề bài, mỗi tiêu chí có $4$ mức điểm: $\\{0; 1; 2; 3\\}$.\\\\
            Gọi $A$ là doanh nghiệp tiềm năng.\\\\
            Tổng điểm $6$ tiêu chí bằng $16 \\Leftrightarrow x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 16 \\quad (*)$\\\\
            Gọi $B$ là doanh nghiệp cân bằng.\\\\
            Các cặp tiêu chí đối diện nhau có điểm bằng nhau $\\Leftrightarrow x_1 = x_4, x_2 = x_5, x_3 = x_6$.\\\\
            Trường hợp doanh nghiệp tiềm năng ($n(A)$):\\\\
            Đặt $y_i = 3 - x_i$. Vì $x_i \\in \\{0; 1; 2; 3\\} \\Rightarrow y_i \\in \\{0; 1; 2; 3\\}$.\\\\
            Thay vào $(*)$ ta có $y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 2$.\\\\
            - Trường hợp 1: Một biến bằng $2$, các biến còn lại bằng $0$ có $C_6^1 = 6$ cách.\\\\
            - Trường hợp 2: Hai biến bằng $1$, các biến còn lại bằng $0$ có $C_6^2 = 15$ cách.\\\\
            Vậy tổng số trường hợp doanh nghiệp tiềm năng là: $n(A) = 6 + 15 = 21$ trường hợp.\\\\
            Trường hợp vừa "Tiềm năng" vừa "Cân bằng" ($n(A \\cap B)$):\\\\
            Để doanh nghiệp cân bằng, ta có $x_1 = x_4, x_2 = x_5, x_3 = x_6$.\\\\
            Thay vào $(*)$ ta được $2x_1 + 2x_2 + 2x_3 = 16 \\Leftrightarrow x_1 + x_2 + x_3 = 8$.\\\\
            Với $x_i \\in \\{0; 1; 2; 3\\}$, các bộ số $(x_1, x_2, x_3)$ có tổng bằng $8$ chỉ có thể là hoán vị của bộ $(3, 3, 2)$.\\\\
            Các bộ thỏa mãn là $(3, 3, 2), (3, 2, 3), (2, 3, 3)$ suy ra $n(A \\cap B) = 3$ trường hợp.\\\\
            Vậy xác suất cần tính là: $P(B|A) = \\frac{n(A \\cap B)}{n(A)} = \\frac{3}{21} = \\frac{1}{7} \\approx 0,14$.''')
                else:
                    kq_exact = "0,05"
                    s_list = ["0,15", "0,10", "0,02", "0,08", "0,20"]
                    loigiai_text = ('''Gọi $x_1, x_2, x_3, x_4, x_5, x_6$ lần lượt là điểm đánh giá của $6$ tiêu chí.\\\\
            Theo đề bài, mỗi tiêu chí có $4$ mức điểm: $\\{0; 1; 2; 3\\}$.\\\\
            Gọi $A$ là doanh nghiệp tiềm năng.\\\\
            Tổng điểm $6$ tiêu chí bằng $14 \\Leftrightarrow x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 14 \\quad (*)$\\\\
            Gọi $B$ là doanh nghiệp cân bằng.\\\\
            Các cặp tiêu chí đối diện nhau có điểm bằng nhau $\\Leftrightarrow x_1 = x_4, x_2 = x_5, x_3 = x_6$.\\\\
            Trường hợp doanh nghiệp tiềm năng ($n(A)$):\\\\
            Đặt $y_i = 3 - x_i$. Vì $x_i \\in \\{0; 1; 2; 3\\} \\Rightarrow y_i \\in \\{0; 1; 2; 3\\}$.\\\\
            Thay vào $(*)$ ta có $y_1 + y_2 + y_3 + y_4 + y_5 + y_6 = 4$.\\\\
            - Trường hợp 1: Một biến bằng $3$, một biến bằng $1$, các biến còn lại bằng $0$ có $C_6^1 \\cdot C_5^1 = 30$ cách.\\\\
            - Trường hợp 2: Hai biến bằng $2$, các biến còn lại bằng $0$ có $C_6^2 = 15$ cách.\\\\
            - Trường hợp 3: Một biến bằng $2$, hai biến bằng $1$, các biến còn lại bằng $0$ có $C_6^1 \\cdot C_5^2 = 60$ cách.\\\\
            - Trường hợp 4: Bốn biến bằng $1$, các biến còn lại bằng $0$ có $C_6^4 = 15$ cách.\\\\
            Vậy tổng số trường hợp doanh nghiệp tiềm năng là: $n(A) = 30 + 15 + 60 + 15 = 120$ trường hợp.\\\\
            Trường hợp vừa "Tiềm năng" vừa "Cân bằng" ($n(A \\cap B)$):\\\\
            Để doanh nghiệp cân bằng, ta có $x_1 = x_4, x_2 = x_5, x_3 = x_6$.\\\\
            Thay vào $(*)$ ta được $2x_1 + 2x_2 + 2x_3 = 14 \\Leftrightarrow x_1 + x_2 + x_3 = 7$.\\\\
            Với $x_i \\in \\{0; 1; 2; 3\\}$, các bộ số $(x_1, x_2, x_3)$ có tổng bằng $7$ có thể là hoán vị của bộ $(3, 3, 1)$ hoặc $(3, 2, 2)$.\\\\
            Số bộ thỏa mãn là $3 + 3 = 6$, suy ra $n(A \\cap B) = 6$ trường hợp.\\\\
            Vậy xác suất cần tính là: $P(B|A) = \\frac{n(A \\cap B)}{n(A)} = \\frac{6}{120} = \\frac{1}{20} = 0,05$.''')

                # Các đáp án trắc nghiệm
                da = '$%s$' % kq_exact

                random.shuffle(s_list)
                das1 = '$%s$' % s_list[0]
                das2 = '$%s$' % s_list[1]
                das3 = '$%s$' % s_list[2]

                # TikZ vẽ biểu đồ Radar
                tikz_fig = ('''\\begin{center}
            \\begin{tikzpicture}[scale=0.8, font=\\scriptsize, line width=1pt]
            \\fill[orange!10] (90:3) -- (30:3) -- (-30:3) -- (-90:3) -- (-150:3) -- (150:3) -- cycle;
            \\draw[green, thick] (90:1) -- (30:1) -- (-30:1) -- (-90:1) -- (-150:1) -- (150:1) -- cycle;
            \\draw[purple, thick] (90:2) -- (30:2) -- (-30:2) -- (-90:2) -- (-150:2) -- (150:2) -- cycle;
            \\draw[blue, thick] (90:3) -- (30:3) -- (-30:3) -- (-90:3) -- (-150:3) -- (150:3) -- cycle;
            \\foreach \\a in {90, 30, -30, -90, -150, 150} {
                \\draw[gray, thin] (0,0) -- (\\a:3);}
            \\node[above] at (90:3.2) {Công nghệ};
            \\node[right] at (30:3.2) {Tài chính};
            \\node[right] at (-30:3.2) {Nhân sự};
            \\node[below] at (-90:3.2) {Quy trình};
            \\node[left] at (-150:3.2) {Sản phẩm};
            \\node[left] at (150:3.2) {Thị trường};
            \\node[circle, draw=red, fill=red!20, inner sep=1pt, minimum size=4mm] at (0,0) {0};
            \\foreach \\a in {90, 30, -30, -90, -150, 150} {
                \\node[circle, draw=green, fill=green!20, inner sep=1pt, minimum size=4mm] at (\\a:1) {1};
                \\node[circle, draw=purple, fill=purple!20, inner sep=1pt, minimum size=4mm] at (\\a:2) {2};
                \\node[circle, draw=blue, fill=blue!20, inner sep=1pt, minimum size=4mm] at (\\a:3) {3};}
            \\end{tikzpicture}
            \\end{center}''')

                # Câu hỏi
                noidungcauhoi = ('''Một quỹ đầu tư mạo hiểm đánh giá các Startup dựa trên $6$ tiêu chí bao gồm: Công nghệ, tài chính, nhân sự, quy trình, sản phẩm, thị trường. Kết quả đánh giá được thể hiện trên một biểu đồ Radar lục giác đều (như hình vẽ), trong đó mức độ đánh giá cho mỗi tiêu chí như sau:
            %s
            Mức $0$: yếu (tâm đỏ); mức $1$: khá (vòng xanh lá); mức $2$: tốt (vòng tím); mức $3$: xuất sắc (vòng xanh dương ngoài cùng). Giả sử quá trình đánh giá $6$ tiêu chí là độc lập ngẫu nhiên. Khi đó, doanh nghiệp tiềm năng là doanh nghiệp có tổng điểm của cả $6$ tiêu chí đúng bằng $%s$ điểm và doanh nghiệp cân bằng là doanh nghiệp có điểm số của các cặp tiêu chí đối diện nhau là bằng nhau. Biết rằng một Startup đã được đánh giá là ``Doanh nghiệp tiềm năng''. Xác suất để Startup đó cũng là một ``Doanh nghiệp cân bằng'' bằng bao nhiêu? (Kết quả làm tròn đến hàng phần trăm).''' % (tikz_fig, S))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = loigiai_text
                dapan='\\shortans[0]{$%s$}\n'%(kq_exact)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + dapan+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n\\end{minipage} \n\n')
            return content

