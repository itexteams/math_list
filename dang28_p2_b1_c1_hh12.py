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


def bt_dang28_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện ABCD có P, Q, M, N trên AD và BC chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Không dùng ký hiệu % comment bên trong string để tránh lỗi định dạng chuỗi
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.6);
    \\coordinate (B) at (-1.8,-0.5);
    \\coordinate (C) at (0.6,-1.2);
    \\coordinate (D) at (2.2,-0.5);
    \\coordinate (P) at ($(A)!0.5!(D)$);
    \\coordinate (M) at ($(A)!0.75!(D)$);
    \\coordinate (Q) at ($(B)!0.5!(C)$);
    \\coordinate (N) at ($(B)!0.75!(C)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
    \\draw[line width=1pt, dashed] (B)--(D) (P)--(Q) (M)--(N);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (P) circle (1pt) node[above right] {$P$};
    \\fill (M) circle (1pt) node[below right] {$M$};
    \\fill (Q) circle (1pt) node[below left] {$Q$};
    \\fill (N) circle (1pt) node[below left] {$N$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Trong không gian, cho tứ diện $ABCD$. Trên cạnh $AD$ và $BC$ lần lượt lấy các điểm $M, N$ sao cho $AM = 3MD$ và $BN = 3NC$. Gọi $P, Q$ lần lượt là trung điểm $AD$ và $BC$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{PQ} = \vec{AC} + \vec{DB} (Sai vì 2\vec{PQ} = \vec{AC} + \vec{DB})[cite: 20]
    nb_da_1_d = "\\True $2\\vec{PQ} = \\vec{AC} + \\vec{DB}$"
    nb_da_1_s = "$\\vec{PQ} = \\vec{AC} + \\vec{DB}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $P, Q$ lần lượt là trung điểm của $AD$ và $BC$, ta có: \\\\ $\\vec{PQ} = \\vec{PA} + \\vec{AC} + \\vec{CQ}$. \\\\ $\\vec{PQ} = \\vec{PD} + \\vec{DB} + \\vec{BQ}$. \\\\ Cộng từng vế hai đẳng thức trên, ta được: \\\\ $2\\vec{PQ} = (\\vec{PA} + \\vec{PD}) + \\vec{AC} + \\vec{DB} + (\\vec{CQ} + \\vec{BQ})$. \\\\ Vì $P$ là trung điểm $AD$ nên $\\vec{PA} + \\vec{PD} = \\vec{0}$. \\\\ Vì $Q$ là trung điểm $BC$ nên $\\vec{CQ} + \\vec{BQ} = \\vec{0}$. \\\\ Do đó ta có: $2\\vec{PQ} = \\vec{AC} + \\vec{DB} \\Leftrightarrow \\vec{PQ} = \\frac{1}{2}(\\vec{AC} + \\vec{DB})$. \\\\ Đẳng thức $\\vec{PQ} = \\vec{AC} + \\vec{DB}$ thiếu hệ số $2$ nên là sai. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: M, N lần lượt là trung điểm của PD, QC[cite: 20]
    th_da_1_d = "\\True $M, N$ lần lượt là trung điểm của $PD, QC$"
    th_da_1_s = "$M, N$ lần lượt là trung điểm của $AP, BQ$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Xét cạnh $AD$: \\\\ Do $P$ là trung điểm của $AD$ nên $AP = PD = \\frac{1}{2}AD$. \\\\ Mặt khác, điểm $M$ thuộc đoạn thẳng $AD$ thỏa mãn $AM = 3MD$, suy ra $MD = \\frac{1}{4}AD$. \\\\ Khi đó độ dài đoạn thẳng $PM$ là: \\\\ $PM = PD - MD = \\frac{1}{2}AD - \\frac{1}{4}AD = \\frac{1}{4}AD$. \\\\ Suy ra $PM = MD = \\frac{1}{4}AD$, do đó $M$ là trung điểm của đoạn thẳng $PD$. \\\\ Tương tự trên cạnh $BC$: \\\\ $Q$ là trung điểm của $BC$ nên $QC = \\frac{1}{2}BC$. \\\\ Điểm $N$ thuộc đoạn $BC$ thỏa mãn $BN = 3NC$, suy ra $NC = \\frac{1}{4}BC$. \\\\ Khi đó độ dài đoạn thẳng $QN$ là: \\\\ $QN = QC - NC = \\frac{1}{2}BC - \\frac{1}{4}BC = \\frac{1}{4}BC = NC$. \\\\ Do đó $N$ là trung điểm của đoạn thẳng $QC$. \\\\ Vậy $M, N$ lần lượt là trung điểm của $PD, QC$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{MN} = \vec{MA} + \vec{AC} + \vec{CN} và \vec{MN} = \vec{MD} + \vec{DB} + \vec{BN}[cite: 20]
    vd_da_1_d = (
        "\\True $\\vec{MN} = \\vec{MA} + \\vec{AC} + \\vec{CN}$ và $\\vec{MN} = \\vec{MD} + \\vec{DB} + \\vec{BN}$"
    )
    vd_da_1_s = (
        "$\\vec{MN} = \\vec{MA} + \\vec{AC} + \\vec{NC}$ và $\\vec{MN} = \\vec{MD} + \\vec{DB} + \\vec{BN}$"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Áp dụng quy tắc ba điểm mở rộng cho phép cộng vectơ trong không gian: \\\\ $\\bullet$ Chèn liên tiếp hai điểm $A$ và $C$ vào vectơ $\\vec{MN}$, ta được: \\\\ $\\vec{MN} = \\vec{MA} + \\vec{AC} + \\vec{CN}$. \\\\ $\\bullet$ Chèn liên tiếp hai điểm $D$ và $B$ vào vectơ $\\vec{MN}$, ta được: \\\\ $\\vec{MN} = \\vec{MD} + \\vec{DB} + \\vec{BN}$. \\\\ Cả hai đẳng thức vectơ trên đều hoàn toàn đúng theo quy tắc cộng vectơ. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: 4\vec{MN} = \vec{AC} - 3\vec{BD} (Sai)[cite: 20]
    vdc_da_1_d = "\\True $4\\vec{MN} \\neq \\vec{AC} - 3\\vec{BD}$"
    vdc_da_1_s = "$4\\vec{MN} = \\vec{AC} - 3\\vec{BD}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta biểu diễn vectơ $\\vec{MN}$ qua các vectơ cạnh $\\vec{AD}, \\vec{AC}, \\vec{BD}$: \\\\ Ta có $AM = 3MD \\Rightarrow \\vec{AM} = \\frac{3}{4}\\vec{AD} \\Rightarrow \\vec{MA} = -\\frac{3}{4}\\vec{AD}$ và $\\vec{MD} = \\frac{1}{4}\\vec{AD}$. \\\\ Mặt khác $BN = 3NC \\Rightarrow \\vec{CN} = -\\frac{1}{4}\\vec{BC}$ và $\\vec{BN} = \\frac{3}{4}\\vec{BC}$. \\\\ Áp dụng hai phân tích ở câu c: \\\\ $\\vec{MN} = \\vec{MA} + \\vec{AC} + \\vec{CN} = -\\frac{3}{4}\\vec{AD} + \\vec{AC} - \\frac{1}{4}\\vec{BC}$. \\\\ $\\vec{MN} = \\vec{MD} + \\vec{DB} + \\vec{BN} = \\frac{1}{4}\\vec{AD} - \\vec{BD} + \\frac{3}{4}\\vec{BC}$. \\\\ Nhân đẳng thức thứ hai với $3$ rồi cộng với đẳng thức thứ nhất: \\\\ $4\\vec{MN} = \\left(-\\frac{3}{4}\\vec{AD} + 3 \\cdot \\frac{1}{4}\\vec{AD}\\right) + \\vec{AC} - 3\\vec{BD} + \\left(-\\frac{1}{4}\\vec{BC} + 3 \\cdot \\frac{3}{4}\\vec{BC}\\right)$ \\\\ $\\Leftrightarrow 4\\vec{MN} = \\vec{AC} - 3\\vec{BD} + 2\\vec{BC}$. \\\\ Do còn xuất hiện thêm số hạng $2\\vec{BC} \\neq \\vec{0}$ nên $4\\vec{MN} \\neq \\vec{AC} - 3\\vec{BD}$. \\\\ Do đó khẳng định $4\\vec{MN} = \\vec{AC} - 3\\vec{BD}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vdc_da_1 else "sai")
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
    
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
    
        if 1 <= true_count <= 3:
            break
    
    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    