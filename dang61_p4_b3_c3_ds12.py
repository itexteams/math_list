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


def bt_dang61_p4_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a_val = random.choice([3, 6, 9, 12, 15, 18])

                # Tính toán các đại lượng
                S_val = Rational(a_val**2, 4) * sqrt(3)
                h_val = Rational(a_val, 2) * sqrt(3)

                # Đáp án đúng: 22/27 S
                kq_val = Rational(22, 27) * S_val

                # Các đáp án nhiễu
                kq_sai1 = Rational(17, 27) * S_val # Chỉ tính diện tích cỏ
                kq_sai2 = Rational(5, 27) * S_val  # Chỉ tính diện tích hoa
                kq_sai3 = Rational(19, 27) * S_val # Tính sai hệ số

                # Định dạng LaTeX
                kq_tex = latex(kq_val)

                # Các đáp án trắc nghiệm
                du = ['$%s$' % (kq_tex)]
                da = random.choice(du)

                s = [
                    '$%s$' % (latex(kq_sai1)),
                    '$%s$' % (latex(kq_sai2)),
                    '$%s$' % (latex(kq_sai3)),
                    '$%s$' % (latex(Rational(23, 27) * S_val)),
                    '$%s$' % (latex(Rational(20, 27) * S_val)),
                    '$%s$' % (latex(Rational(16, 27) * S_val))
                ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Hình vẽ TikZ
                tikz_code = '''\\begin{tikzpicture}[line width=1pt, scale=0.8]
            \\def\\sq{1.73205}
            \\coordinate (O) at (0,\\sq);
            \\coordinate (A) at (0,3*\\sq);
            \\coordinate (B) at (-3,0);
            \\coordinate (C) at (3,0);
            \\coordinate (I1) at (-1,4*\\sq/3);
            \\coordinate (I2) at (1,4*\\sq/3);
            \\coordinate (I3) at (0,\\sq/3);
            \\def\\pathOne{(B) .. controls (-1, {2*\\sq}) and (1, {2*\\sq}) .. (C) -- cycle}
            \\def\\pathTwo{(C) .. controls (-1, 0) and (-2, \\sq) .. (A) -- cycle}
            \\def\\pathThree{(A) .. controls (2, \\sq) and (1, 0) .. (B) -- cycle}
            \\begin{scope} \\clip (B) .. controls (-1, {2*\\sq}) and (1, {2*\\sq}) .. (C) -- cycle; \\fill[green!40] (C) .. controls (-1, 0) and (-2, \\sq) .. (A) -- cycle; \\end{scope}
            \\begin{scope} \\clip (C) .. controls (-1, 0) and (-2, \\sq) .. (A) -- cycle; \\fill[green!40] (A) .. controls (2, \\sq) and (1, 0) .. (B) -- cycle; \\end{scope}
            \\begin{scope} \\clip (A) .. controls (2, \\sq) and (1, 0) .. (B) -- cycle; \\fill[green!40] (B) .. controls (-1, {2*\\sq}) and (1, {2*\\sq}) .. (C) -- cycle; \\end{scope}
            \\begin{scope} 
            \\clip (B) .. controls (-1, {2*\\sq}) and (1, {2*\\sq}) .. (C) -- cycle; 
            \\clip (C) .. controls (-1, 0) and (-2, \\sq) .. (A) -- cycle; 
            \\fill[purple!30] (A) .. controls (2, \\sq) and (1, 0) .. (B) -- cycle; 
            \\end{scope}
            \\draw (B) .. controls (-1, {2*\\sq}) and (1, {2*\\sq}) .. (C);
            \\draw (C) .. controls (-1, 0) and (-2, \\sq) .. (A);
            \\draw (A) .. controls (2, \\sq) and (1, 0) .. (B);
            \\draw[dashed] (A) -- (B) -- (C) -- cycle;
            \\draw[dashed] (A) -- (0,0);
            \\draw[dashed, blue] (I1) -- (I2) -- (I3) -- cycle;
            \\draw[dashed, blue] (O) -- (I1);
            \\draw[dashed, blue] (O) -- (I2);
            \\draw[dashed, blue] (O) -- (I3);
            \\fill (A) circle (1.5pt) node[above] {$A$};
            \\fill (B) circle (1.5pt) node[left] {$B$};
            \\fill (C) circle (1.5pt) node[right] {$C$};
            \\fill[red] (O) circle (1.5pt) node[below right, yshift=2pt] {$O$};
            \\fill[red] (I1) circle (1.5pt) node[left] {$I_1$};
            \\fill[red] (I2) circle (1.5pt) node[right] {$I_2$};
            \\fill[red] (I3) circle (1.5pt) node[below] {$I_3$};
            \\end{tikzpicture}'''

                # Câu hỏi
                noidungcauhoi = ('''\\immini{Một khu vườn có dạng tam giác đều $ABC$ cạnh bằng $%s$ m. Người ta thiết kế khu vườn bằng cách vẽ ba đường parabol $\\left(P_1\\right), \\left(P_2\\right), \\left(P_3\\right)$ sao cho $\\left(P_1\\right)$ có trục đối xứng là đường thẳng $OA$, tiếp xúc với hai cạnh $AB, AC$ lần lượt tại $B$ và $C$. Tương tự $\\left(P_2\\right)$ tiếp xúc với hai cạnh $BC, BA$ lần lượt tại $C$ và $A$ và $\\left(P_3\\right)$ tiếp xúc với hai cạnh $CA, CB$ lần lượt tại $A$ và $B$. Ba đường parabol này cắt nhau tại ba điểm $I_1, I_2, I_3$ tạo thành một vùng khép kín ở chính giữa khu vườn để trồng hoa. Phần diện tích trồng cỏ gồm ba vùng khép kín: vùng thứ nhất giới hạn bởi hai cung parabol của $\\left(P_2\\right)$ và $\\left(P_3\\right)$; vùng thứ hai giới hạn bởi hai cung parabol của $\\left(P_1\\right)$ và $\\left(P_3\\right)$; vùng thứ ba giới hạn bởi hai cung parabol của $\\left(P_1\\right)$ và $\\left(P_2\\right)$. Tính tổng diện tích của hai vùng trồng cỏ và hoa.}
            {%s}''' % (a_val, tikz_code))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''Gọi $a = %s$ là độ dài cạnh của tam giác đều $ABC$. Diện tích tam giác $ABC$ là $S = \\frac{a^2\\sqrt{3}}{4} = %s$. \\\\
            Gắn hệ trục toạ độ $Oxy$ với gốc $O$ là trung điểm của $BC$, tia $Ox$ trùng với tia $OC$, tia $Oy$ chứa đường cao $AH$. \\\\
            Khi đó $C\\left(\\frac{a}{2}; 0\\right)$, $B\\left(-\\frac{a}{2}; 0\\right)$, $A\\left(0; h\\right)$ với $h = \\frac{a\\sqrt{3}}{2} = %s$. \\\\
            Đường parabol $\\left(P_2\\right)$ tiếp xúc với $BC$ tại $C$ và $BA$ tại $A$. Dựa vào các tính chất tiếp tuyến, phương trình của $\\left(P_2\\right)$ có dạng $x = \\frac{a}{2}\\left(3\\frac{y}{h} - 4\\sqrt{\\frac{y}{h}} + 1\\right)$. \\\\
            Tương tự, parabol $\\left(P_3\\right)$ tiếp xúc với $BC$ tại $B$ và $CA$ tại $A$ có phương trình $x = \\frac{a}{2}\\left(-3\\frac{y}{h} + 4\\sqrt{\\frac{y}{h}} - 1\\right)$. \\\\
            Phần diện tích giao nhau của các parabol tạo ra $3$ vùng không trồng cỏ và hoa (màu trắng) ở $3$ cạnh tam giác. \\\\
            Xét vùng trắng giới hạn bởi $\\left(P_2\\right), \\left(P_3\\right)$ và cạnh $BC$. Giao điểm của $\\left(P_2\\right)$ và $\\left(P_3\\right)$ có tung độ thoả mãn $x_{\\left(P_2\\right)} = x_{\\left(P_3\\right)} \\Rightarrow 3\\frac{y}{h} - 4\\sqrt{\\frac{y}{h}} + 1 = 0 \\Rightarrow \\sqrt{\\frac{y}{h}} = \\frac{1}{3}$ (chọn nghiệm nhỏ hơn để lấy giao điểm $I_3$ gần $BC$). Suy ra $y = \\frac{h}{9}$. \\\\
            Diện tích của vùng trắng này là: \\\\
            $W_1 = \\int_0^{\\frac{h}{9}} \\left(x_{\\left(P_2\\right)} - x_{\\left(P_3\\right)}\\right) \\text{d}y = \\int_0^{\\frac{h}{9}} a \\left(3\\frac{y}{h} - 4\\sqrt{\\frac{y}{h}} + 1\\right) \\text{d}y$. \\\\
            Đặt $t = \\sqrt{\\frac{y}{h}} \\Rightarrow y = ht^2 \\Rightarrow \\text{d}y = 2ht \\text{d}t$. Khi $y=\\frac{h}{9}$ thì $t=\\frac{1}{3}$. \\\\
            $W_1 = a \\int_0^{\\frac{1}{3}} \\left(3t^2 - 4t + 1\\right) 2ht \\text{d}t = 2ah \\left[ \\frac{3}{4}t^4 - \\frac{4}{3}t^3 + \\frac{1}{2}t^2 \\right]_0^{\\frac{1}{3}} = 2ah \\cdot \\frac{5}{324} = ah \\frac{5}{162}$. \\\\
            Do $ah = 2S$, nên $W_1 = 2S \\cdot \\frac{5}{162} = \\frac{5}{81} S$. \\\\
            Vì tính đối xứng, $3$ vùng trắng có diện tích bằng nhau. Tổng diện tích $3$ vùng trắng là $3 \\cdot \\frac{5}{81} S = \\frac{5}{27} S$. \\\\
            Tổng diện tích của hai vùng trồng cỏ và hoa (tức là toàn bộ phần diện tích được tô màu) là phần diện tích tam giác bỏ đi $3$ vùng trắng: \\\\
            $S_{\\text{cỏ + hoa}} = S - \\frac{5}{27} S = \\frac{22}{27} S = \\frac{22}{27} \\cdot %s = %s$ m$^2$.''' % (a_val, latex(S_val), latex(h_val), latex(S_val), kq_tex))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n\\end{minipage} \n\n')
            return content

