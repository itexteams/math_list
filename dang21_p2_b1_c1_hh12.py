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


def bt_dang21_p2_b1_c1_hh12(self):
    # Mã vẽ TikZ hình hộp ABCD.A'B'C'D' có I, K là tâm các hình bình hành ABB'A' và BCC'B' đúng 100% như ảnh[cite: 21]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (B) at (0,0);
    \\coordinate (C) at (3.2,-0.6);
    \\coordinate (A) at (1.2,1.2);
    \\coordinate (D) at ($(A)+(C)-(B)$);
    \\coordinate (B') at (0.6,2.8);
    \\coordinate (A') at ($(A)+(B')-(B)$);
    \\coordinate (C') at ($(C)+(B')-(B)$);
    \\coordinate (D') at ($(D)+(B')-(B)$);
    \\coordinate (I) at ($(B)!0.5!(A')$);
    \\coordinate (K) at ($(B')!0.5!(C)$);
    \\draw[line width=1pt] (B)--(C)--(D)--(D')--(A')--(B')--cycle;
    \\draw[line width=1pt] (B')--(C')--(D') (C)--(C') (B')--(C) (A')--(C');
    \\draw[line width=1pt, dashed] (B)--(A)--(D) (A)--(A') (A)--(C) (B)--(D) (A')--(B) (A)--(B') (B)--(C') (A')--(D) (I)--(K);
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (B') circle (1pt) node[above left] {$B'$};
    \\fill (A') circle (1pt) node[above] {$A'$};
    \\fill (C') circle (1pt) node[above right] {$C'$};
    \\fill (D') circle (1pt) node[above right] {$D'$};
    \\fill (I) circle (1pt) node[left] {$I$};
    \\fill (K) circle (1pt) node[above] {$K$};
    \\end{tikzpicture}
    \\end{center}"""
    
    # Nội dung câu hỏi[cite: 21]
    noidungcauhoi = (
        """Cho hình hộp $ABCD.A'B'C'D'$. Gọi $I$ và $K$ lần lượt là tâm của hình bình hành $ABB'A'$ và $BCC'B'$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: \vec{IK} = 1/2 \vec{AC} = 1/2 \vec{A'C'} (Đúng)[cite: 21]
    nb_da_1_d = "\\True $\\vec{IK} = \\frac{1}{2}\\vec{AC} = \\frac{1}{2}\\vec{A'C'}$"
    nb_da_1_s = "$\\vec{IK} = \\vec{AC} = \\vec{A'C'}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Vì $I$ là tâm hình bình hành $ABB'A'$ nên $I$ là trung điểm của $A'B$. \\\\ Vì $K$ là tâm hình bình hành $BCC'B'$ nên $K$ là trung điểm của $BC'$. \\\\ Xét tam giác $BA'C'$, đoạn thẳng $IK$ là đường trung bình ứng với cạnh $A'C'$, do đó: \\\\ $\\vec{IK} = \\frac{1}{2}\\vec{A'C'}$. \\\\ Mặt khác, vì tứ giác $ACC'A'$ là hình bình hành nên $\\vec{A'C'} = \\vec{AC}$. \\\\ Suy ra $\\vec{IK} = \\frac{1}{2}\\vec{AC} = \\frac{1}{2}\\vec{A'C'}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: Bốn điểm I, K, C, A đồng phẳng (Đúng do IK // AC)[cite: 21]
    th_da_1_d = "\\True Bốn điểm $I, K, C, A$ đồng phẳng"
    th_da_1_s = "Bốn điểm $I, K, C, A$ không đồng phẳng"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Theo kết quả câu a, ta có $\\vec{IK} = \\frac{1}{2}\\vec{AC}$, suy ra đường thẳng $IK$ song song với đường thẳng $AC$ ($IK // AC$). \\\\ Do hai đường thẳng $IK$ và $AC$ song song với nhau nên chúng cùng thuộc một mặt phẳng duy nhất. \\\\ Suy ra bốn điểm $I, K, C, A$ cùng thuộc một mặt phẳng (đồng phẳng). \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{BD} + 2\vec{IK} = 2\vec{BC} (Đúng)[cite: 21]
    vd_da_1_d = "\\True $\\vec{BD} + 2\\vec{IK} = 2\\vec{BC}$"
    vd_da_1_s = "$\\vec{BD} + 2\\vec{IK} = \\vec{BC}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Ta có $\\vec{IK} = \\frac{1}{2}\\vec{AC} \\Leftrightarrow 2\\vec{IK} = \\vec{AC}$. \\\\ Khi đó vế trái của đẳng thức là: \\\\ $\\vec{BD} + 2\\vec{IK} = \\vec{BD} + \\vec{AC}$. \\\\ Phân tích hai vectơ theo hai vectơ cạnh đáy $\\vec{AB}$ và $\\vec{BC}$: \\\\ $\\bullet$ $\\vec{BD} = \\vec{BA} + \\vec{BC} = -\\vec{AB} + \\vec{BC}$. \\\\ $\\bullet$ $\\vec{AC} = \\vec{AB} + \\vec{BC}$. \\\\ Do đó: \\\\ $\\vec{BD} + 2\\vec{IK} = (-\\vec{AB} + \\vec{BC}) + (\\vec{AB} + \\vec{BC}) = 2\\vec{BC}$. \\\\ Khẳng định $\\vec{BD} + 2\\vec{IK} = 2\\vec{BC}$ là đúng. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Ba vectơ \vec{BD}; \vec{IK}; \vec{B'C'} không đồng phẳng (Sai, vì chúng đồng phẳng)[cite: 21]
    vdc_da_1_d = "\\True Ba vectơ $\\vec{BD}; \\vec{IK}; \\vec{B'C'}$ đồng phẳng"
    vdc_da_1_s = "Ba vectơ $\\vec{BD}; \\vec{IK}; \\vec{B'C'}$ không đồng phẳng"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta biểu diễn các vectơ $\\vec{BD}, \\vec{IK}, \\vec{B'C'}$ qua hai vectơ không cùng phương là $\\vec{BA}$ và $\\vec{BC}$ thuộc mặt phẳng đáy $(ABCD)$: \\\\ $\\bullet$ $\\vec{BD} = \\vec{BA} + \\vec{BC}$. \\\\ $\\bullet$ $\\vec{IK} = \\frac{1}{2}\\vec{AC} = \\frac{1}{2}(\\vec{AB} + \\vec{BC}) = -\\frac{1}{2}\\vec{BA} + \\frac{1}{2}\\vec{BC}$. \\\\ $\\bullet$ $\\vec{B'C'} = \\vec{BC} = 0\\vec{BA} + 1\\vec{BC}$. \\\\ Nhận thấy giá của cả ba vectơ $\\vec{BD}, \\vec{IK}, \\vec{B'C'}$ đều song song hoặc nằm trong mặt phẳng $(ABCD)$. \\\\ Cụ thể, ta có phân tích: \\\\ $\\vec{BD} = -2\\vec{IK} + 2\\vec{B'C'}$. \\\\ Do tồn tại cặp số thực $(-2; 2)$ thỏa mãn hệ thức phân tích nên ba vectơ $\\vec{BD}; \\vec{IK}; \\vec{B'C'}$ đồng phẳng. \\\\ Khẳng định ba vectơ không đồng phẳng là sai. \\\\ Do đó mệnh đề là %s."""
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
    