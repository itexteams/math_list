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


def bt_dang43_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện ABCD có E, F là trung điểm AB, CD; I là trung điểm EF; G là trọng tâm tam giác BCD chuẩn 100% như ảnh[cite: 21]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi định dạng chuỗi
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,3.2);
    \\coordinate (B) at (-1.6,-0.1);
    \\coordinate (C) at (-0.3,-1.5);
    \\coordinate (D) at (2.4,-0.1);
    \\coordinate (E) at ($(A)!0.5!(B)$);
    \\coordinate (F) at ($(C)!0.5!(D)$);
    \\coordinate (I) at ($(E)!0.5!(F)$);
    \\coordinate (G) at ($(B)!0.66667!(F)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
    \\draw[line width=1pt] (A)--(F);
    \\draw[line width=1pt, dashed] (B)--(D) (E)--(F) (A)--(G) (B)--(F);
    \\draw[line width=0.8pt] ($(G)+(0,0.25)$) -- ($(G)+(0.2,0.25)$) -- ($(G)+(0.2,0.05)$);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (E) circle (1pt) node[above left] {$E$};
    \\fill (F) circle (1pt) node[below] {$F$};
    \\fill (I) circle (1pt) node[above right] {$I$};
    \\fill (G) circle (1pt) node[below] {$G$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Random độ dài cạnh của tứ diện đều cho ý d[cite: 21]
    s_val = random.choice([3, 6, 9])
    # Q_min = 5 * s^2 / 3
    q_min_true = 5 * (s_val**2) // 3
    q_min_false = q_min_true - random.choice([3, 5, 6])
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Trong không gian với hệ tọa độ $Oxyz$, cho tứ diện $ABCD$ có $E, F$ lần lượt là trung điểm của các cạnh $AB, CD$. Điểm $I$ là trung điểm của $EF$ và $G$ là trọng tâm của tam giác $BCD$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{IA} + \vec{IB} + \vec{IC} + \vec{ID} = \vec{0}[cite: 21]
    nb_da_1_d = "\\True $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = \\vec{0}$"
    nb_da_1_s = "$\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = 2\\vec{EF}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $E$ là trung điểm của đoạn thẳng $AB$ nên với điểm $I$ ta có: \\\\ $\\vec{IA} + \\vec{IB} = 2\\vec{IE}$. \\\\ Vì $F$ là trung điểm của đoạn thẳng $CD$ nên với điểm $I$ ta có: \\\\ $\\vec{IC} + \\vec{ID} = 2\\vec{IF}$. \\\\ Cộng vế theo vế hai đẳng thức trên, ta được: \\\\ $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = 2(\\vec{IE} + \\vec{IF})$. \\\\ Mặt khác, vì $I$ là trung điểm của đoạn thẳng $EF$ nên $\\vec{IE} + \\vec{IF} = \\vec{0}$. \\\\ Suy ra: \\\\ $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = 2 \\cdot \\vec{0} = \\vec{0}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{AB} + \vec{AC} + \vec{AD} = 4\vec{AI} (sai nếu là 3\vec{AI})[cite: 21]
    th_da_1_d = "\\True $\\vec{AB} + \\vec{AC} + \\vec{AD} = 4\\vec{AI}$"
    th_da_1_s = "$\\vec{AB} + \\vec{AC} + \\vec{AD} = 3\\vec{AI}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Theo kết quả ở câu a, điểm $I$ là trọng tâm của tứ diện $ABCD$, do đó thỏa mãn hệ thức: \\\\ $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = \\vec{0}$. \\\\ Chèn điểm gốc $A$ vào hệ thức vectơ trên: \\\\ $(-\\vec{AI}) + (\\vec{AB} - \\vec{AI}) + (\\vec{AC} - \\vec{AI}) + (\\vec{AD} - \\vec{AI}) = \\vec{0}$ \\\\ $\\Leftrightarrow \\vec{AB} + \\vec{AC} + \\vec{AD} - 4\\vec{AI} = \\vec{0}$ \\\\ $\\Leftrightarrow \\vec{AB} + \\vec{AC} + \\vec{AD} = 4\\vec{AI}$. \\\\ Khẳng định $\\vec{AB} + \\vec{AC} + \\vec{AD} = 3\\vec{AI}$ là sai do hệ số đúng phải bằng $4$. \\\\ Do đó khẳng định là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Biểu thức P = |\vec{MA} + \vec{MB} + \vec{MC} + \vec{MD}| đạt giá trị nhỏ nhất <=> M trùng I (đúng) hoặc M trùng G (sai)[cite: 21]
    vd_da_1_d = "\\True Biểu thức $P = |\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD}|$ đạt giá trị nhỏ nhất $\\Leftrightarrow M \\equiv I$"
    vd_da_1_s = "Biểu thức $P = |\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD}|$ đạt giá trị nhỏ nhất $\\Leftrightarrow M \\equiv G$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $I$ là trọng tâm của tứ diện $ABCD$ nên $\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID} = \\vec{0}$. \\\\ Chèn điểm $I$ vào biểu thức tổng bốn vectơ, ta có: \\\\ $\\vec{MA} + \\vec{MB} + \\vec{MC} + \\vec{MD} = (\\vec{MI} + \\vec{IA}) + (\\vec{MI} + \\vec{IB}) + (\\vec{MI} + \\vec{IC}) + (\\vec{MI} + \\vec{ID})$ \\\\ $= 4\\vec{MI} + (\\vec{IA} + \\vec{IB} + \\vec{IC} + \\vec{ID}) = 4\\vec{MI}$. \\\\ Do đó độ lớn của biểu thức $P$ là: \\\\ $P = |4\\vec{MI}| = 4MI$. \\\\ Vì độ dài đoạn thẳng $MI \\ge 0$ nên $P \\ge 0$. \\\\ Giá trị nhỏ nhất của $P$ bằng $0$, đạt được khi và chỉ khi $MI = 0 \\Leftrightarrow M \\equiv I$. \\\\ Khẳng định biểu thức đạt giá trị nhỏ nhất khi $M \\equiv G$ là sai. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Q = NA^2 + NB^2 + NC^2 + ND^2 đạt GTNN bằng 5s^2/3 khi N trên (BCD)[cite: 21]
    vdc_da_1_d = (
        "\\True Giả sử tứ diện $ABCD$ đều có cạnh bằng $%s$ và $N$ là một điểm thay đổi trên mặt phẳng $(BCD)$. Khi đó biểu thức $Q = NA^2 + NB^2 + NC^2 + ND^2$ đạt giá trị nhỏ nhất bằng $%s$"
        % (s_val, q_min_true)
    )
    vdc_da_1_s = (
        "Giả sử tứ diện $ABCD$ đều có cạnh bằng $%s$ và $N$ là một điểm thay đổi trên mặt phẳng $(BCD)$. Khi đó biểu thức $Q = NA^2 + NB^2 + NC^2 + ND^2$ đạt giá trị nhỏ nhất bằng $%s$"
        % (s_val, q_min_false)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Vì $G$ là trọng tâm tam giác đều $BCD$ nên với điểm $N$ bất kỳ ta có: \\\\ $NB^2 + NC^2 + ND^2 = 3NG^2 + GB^2 + GC^2 + GD^2$. \\\\ Trong tứ diện đều $ABCD$ cạnh $s = %s$: \\\\ $\\bullet$ Mặt phẳng đáy $BCD$ là tam giác đều cạnh $%s$ nên bán kính đường tròn ngoại tiếp tam giác đáy là: \\\\ $GB = GC = GD = \\frac{s\\sqrt{3}}{3} = \\frac{%s\\sqrt{3}}{3} \\Rightarrow GB^2 = GC^2 = GD^2 = \\frac{s^2}{3} = %s$. \\\\ $\\Rightarrow GB^2 + GC^2 + GD^2 = 3 \\cdot %s = %s$. \\\\ $\\bullet$ Đoạn thẳng $AG$ vuông góc với mặt phẳng đáy $(BCD)$ tại tâm $G$, do đó tam giác $AGN$ vuông tại $G$. Áp dụng định lý Pythagore: \\\\ $NA^2 = AG^2 + NG^2$. \\\\ Trong tam giác vuông $AGB$: \\\\ $AG^2 = AB^2 - GB^2 = s^2 - \\frac{s^2}{3} = \\frac{2s^2}{3} = %s$. \\\\ Khi đó biểu thức $Q$ trở thành: \\\\ $Q = NA^2 + (NB^2 + NC^2 + ND^2) = (AG^2 + NG^2) + (3NG^2 + GB^2 + GC^2 + GD^2)$ \\\\ $= 4NG^2 + AG^2 + GB^2 + GC^2 + GD^2 = 4NG^2 + %s + %s = 4NG^2 + %s$. \\\\ Vì $N \\in (BCD)$ nên $NG \\ge 0$, do đó $Q \\ge %s$. \\\\ Dấu đẳng thức xảy ra khi và chỉ khi $NG = 0 \\Leftrightarrow N \\equiv G$. \\\\ Vậy giá trị nhỏ nhất của biểu thức $Q$ bằng $%s$. \\\\ Do đó khẳng định là %s."""
        % (
            s_val,
            s_val,
            s_val,
            s_val**2 // 3,
            s_val**2 // 3,
            s_val**2,
            2 * (s_val**2) // 3,
            2 * (s_val**2) // 3,
            s_val**2,
            q_min_true,
            q_min_true,
            q_min_true,
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
    