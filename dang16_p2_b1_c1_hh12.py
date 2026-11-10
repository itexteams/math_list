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


def bt_dang16_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình hộp chữ nhật ABCD.A'B'C'D' 100% như ảnh[cite: 21]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (2.2,0);
    \\coordinate (D) at (1,1.2);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (A') at (0,2.8);
    \\coordinate (B') at ($(B)+(A')-(A)$);
    \\coordinate (C') at ($(C)+(A')-(A)$);
    \\coordinate (D') at ($(D)+(A')-(A)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(C')--(D')--(A')--cycle;
    \\draw[line width=1pt] (A')--(B')--(C') (B)--(B');
    \\draw[line width=1pt, dashed] (A)--(D)--(C) (D)--(D');
    \\fill (A) circle (1pt) node[below left] {$A$};
    \\fill (B) circle (1pt) node[below] {$B$};
    \\fill (C) circle (1pt) node[right] {$C$};
    \\fill (D) circle (1pt) node[left] {$D$};
    \\fill (A') circle (1pt) node[left] {$A'$};
    \\fill (B') circle (1pt) node[above left] {$B'$};
    \\fill (C') circle (1pt) node[above] {$C'$};
    \\fill (D') circle (1pt) node[above] {$D'$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Sinh ngẫu nhiên kích thước hình hộp chữ nhật có đáy là hình vuông AB = AD = a, chiều cao AA' = h[cite: 21]
    while True:
        a_len = random.choice([1, 2, 3])
        h_len = random.choice([2, 3, 4])
    
        # Độ dài đường chéo A'C = sqrt(AB^2 + AD^2 + AA'^2) = sqrt(2*a^2 + h^2)[cite: 21]
        ac_prime_sq = 2 * (a_len**2) + h_len**2
        ac_prime_sym = sp.sqrt(ac_prime_sq)
        str_ac_prime_true = latex(ac_prime_sym)
    
        # Giá trị sai cho độ dài A'C (như trong đề gốc bình phương lên là 6 hoặc nhầm công thức)[cite: 21]
        str_ac_prime_false = str(ac_prime_sq) if ac_prime_sym != ac_prime_sq else str(ac_prime_sq + 2)
    
        if a_len != h_len:
            break
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Cho hình hộp chữ nhật $ABCD.A'B'C'D'$ có $AB = AD = %s$ và $AA' = %s$. %s"""
        % (a_len, h_len, tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Khẳng định a: Hai vectơ AD' và C'B là cùng phương (Đúng vì AD' // BC')[cite: 21]
    nb_da_1_d = "\\True Hai vectơ $\\vec{AD'}$ và $\\vec{C'B}$ là cùng phương"
    nb_da_1_s = "Hai vectơ $\\vec{AD'}$ và $\\vec{C'B}$ không cùng phương"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Xét tứ giác $ABC'D'$, ta có: \\\\ $\\vec{AB} = \\vec{D'C'} \\Rightarrow ABC'D'$ là hình bình hành. \\\\ Do đó $AD' // BC'$, suy ra hai giá của hai vectơ $\\vec{AD'}$ và $\\vec{C'B}$ song song với nhau. \\\\ Theo định nghĩa, hai vectơ có giá song song là hai vectơ cùng phương. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Khẳng định b: Hai vectơ AB và C'D' bằng nhau (Sai vì C'D' ngược hướng với AB, \vec{AB} = \vec{D'C'} = -\vec{C'D'})[cite: 21]
    th_da_1_d = "\\True Hai vectơ $\\vec{AB}$ và $\\vec{D'C'}$ bằng nhau"
    th_da_1_s = "Hai vectơ $\\vec{AB}$ và $\\vec{C'D'}$ bằng nhau"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Trong hình chữ nhật $A'B'C'D'$, ta có cạnh $A'B'$ song song và bằng cạnh $D'C'$, do đó $\\vec{A'B'} = \\vec{D'C'}$. \\\\ Mặt khác, vì $ABB'A'$ là hình chữ nhật nên $\\vec{AB} = \\vec{A'B'}$. \\\\ Suy ra $\\vec{AB} = \\vec{D'C'}$. \\\\ Do đó hai vectơ $\\vec{AB}$ và $\\vec{C'D'}$ là hai vectơ đối nhau (ngược hướng nhau), tức là $\\vec{AB} = -\\vec{C'D'} \\neq \\vec{C'D'}$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Khẳng định c: Số vectơ khác vectơ không có điểm đầu và điểm cuối là các đỉnh của hình hộp cùng hướng với vectơ BM là 4[cite: 21]
    # BM cùng hướng với các cạnh bên theo chiều từ dưới lên trên: \vec{AA'}, \vec{BB'}, \vec{CC'}, \vec{DD'} (có đúng 4 vectơ)[cite: 21]
    vd_da_1_d = (
        "\\True Gọi $M$ là trung điểm của $BB'$. Số vectơ khác vectơ-không có điểm đầu và điểm cuối là các đỉnh của hình hộp, cùng hướng với vectơ $\\vec{BM}$ là $4$"
    )
    vd_da_1_s = (
        "Gọi $M$ là trung điểm của $BB'$. Số vectơ khác vectơ-không có điểm đầu và điểm cuối là các đỉnh của hình hộp, cùng hướng với vectơ $\\vec{BM}$ là $3$"
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $M$ là trung điểm của đoạn thẳng $BB'$ nên điểm $M$ thuộc đoạn thẳng $BB'$. \\\\ Do đó vectơ $\\vec{BM}$ cùng hướng với vectơ $\\vec{BB'}$. \\\\ Trong hình hộp chữ nhật $ABCD.A'B'C'D'$, các cạnh bên đôi một song song và cùng hướng từ mặt đáy dưới lên mặt đáy trên, gồm các vectơ: \\\\ $\\vec{AA'}, \\vec{BB'}, \\vec{CC'}, \\vec{DD'}$. \\\\ Các vectơ này đều có điểm đầu và điểm cuối là các đỉnh của hình hộp chữ nhật và cùng hướng với vectơ $\\vec{BM}$. \\\\ Có tất cả đúng $4$ vectơ thỏa mãn điều kiện. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Khẳng định d: Độ dài vectơ A'C bằng str_ac_prime_true[cite: 21]
    vdc_da_1_d = "\\True Độ dài vectơ $\\vec{A'C}$ bằng $%s$" % (str_ac_prime_true)
    vdc_da_1_s = "Độ dài vectơ $\\vec{A'C}$ bằng $%s$" % (str_ac_prime_false)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Độ dài của vectơ $\\vec{A'C}$ chính là độ dài đường chéo $A'C$ của hình hộp chữ nhật $ABCD.A'B'C'D'$. \\\\ Áp dụng định lý Pythagore trong không gian, ta có: \\\\ $|\\vec{A'C}| = A'C = \\sqrt{AB^2 + AD^2 + AA'^2} = \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\sqrt{%s + %s + %s} = \\sqrt{%s} = %s$. \\\\ Do đó khẳng định là %s."""
        % (
            a_len,
            a_len,
            h_len,
            a_len**2,
            a_len**2,
            h_len**2,
            ac_prime_sq,
            str_ac_prime_true,
            "đúng" if "\\True" in vdc_da_1 else "sai",
        )
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
    