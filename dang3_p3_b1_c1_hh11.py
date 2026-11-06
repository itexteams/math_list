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


def bt_dang3_p3_b1_c1_hh11(self):
    # Dạng: (m, n, "Nội dung câu hỏi mô tả G", "Lý do trong lời giải") tương ứng với SG/SE = m/n
    configs = [
        (2, 3, "$G$ là trọng tâm của tam giác $SAB$", "($G$ là trọng tâm của tam giác $SAB$)"),
        (3, 4, "$G$ là điểm trên trung tuyến kẻ từ $S$ của tam giác $SAB$ sao cho $\\frac{SG}{SE}=\\frac{3}{4}$ (với $E$ là trung điểm của $AB$)", "(giả thiết)"),
        (3, 5, "$G$ là điểm trên trung tuyến kẻ từ $S$ của tam giác $SAB$ sao cho $\\frac{SG}{SE}=\\frac{3}{5}$ (với $E$ là trung điểm của $AB$)", "(giả thiết)"),
        (4, 5, "$G$ là điểm trên trung tuyến kẻ từ $S$ của tam giác $SAB$ sao cho $\\frac{SG}{SE}=\\frac{4}{5}$ (với $E$ là trung điểm của $AB$)", "(giả thiết)"),
        (5, 7, "$G$ là điểm trên trung tuyến kẻ từ $S$ của tam giác $SAB$ sao cho $\\frac{SG}{SE}=\\frac{5}{7}$ (với $E$ là trung điểm của $AB$)", "(giả thiết)")
    ]

    m, n, text_G, reason_G = random.choice(configs)

    # Tính k
    k_val = Rational(n, 2*m - n)
    k_str = latex(k_val)

    # Các đáp án trắc nghiệm
    du = ['$%s$' % (k_str)]
    da = du[0]

    # Tạo các phương án sai ngẫu nhiên
    wrong_vals = [
        Rational(n, 2*m + n),
        Rational(2*m, n),
        Rational(n, abs(m - n)) if m != n else Rational(1, 2),
        Rational(2*m - n, n),
        k_val + 1,
        abs(k_val - 1)
    ]

    s = []
    for val in wrong_vals:
        ans = '$%s$' % (latex(val))
        if ans not in s and ans != da:
            s.append(ans)

    random.shuffle(s)
    das1 = s[0]
    das2 = s[1]
    das3 = s[2]

    # Câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$, trong đó $ABCD$ là một hình thang với đáy $AB$ và $CD$. Gọi $I$ và $J$ lần lượt là trung điểm của $AD$ và $BC$, %s. Giao tuyến $d$ của hai mặt phẳng $(SAB)$ và $(GIJ)$. Biết $d$ cắt $SA$ tại $M$ và cắt $SB$ tại $N$. Tứ giác $MNJI$ là hình bình hành thì $AB = kCD$. Giá trị của $k$ bằng bao nhiêu?'''
                     % (text_G))

    # Các đáp án
    da_d = ('\\True ' + str(da))
    da_s1 = str(das1)
    da_s2 = str(das2) 
    da_s3 = str(das3) 

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_1 = [da_d, da_s1, da_s2, da_s3]
    random.shuffle(list_1)

    # Xử lý chuỗi hệ số thông minh để tránh việc in ra "1 AB"
    v_2m_n_AB = f"{2*m - n} AB" if (2*m - n) != 1 else "AB"

    # Nội dung lời giải
    loigiai = ('''\\begin{center}
    \\begin{tikzpicture}[line join=round, line cap=round, thick]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (6,0);
    \\coordinate (D) at (1,-2);
    \\coordinate (C) at (4,-2);
    \\coordinate (S) at (2,3);
    \\coordinate (E) at (3,0);
    \\coordinate (I) at (0.5,-1);
    \\coordinate (J) at (5,-1);
    \\coordinate (M) at (0.67,1);
    \\coordinate (N) at (4.67,1);
    \\coordinate (G) at (2.67,1);
    \\draw (A) node[left]{$A$} -- (D) node[below left]{$D$} -- (C) node[below right]{$C$} -- (B) node[right]{$B$};
    \\draw (S) node[above]{$S$} -- (A);
    \\draw (S) -- (D);
    \\draw (S) -- (C);
    \\draw (S) -- (B);
    \\draw (I) node[left]{$I$} -- (M) node[left]{$M$};
    \\draw (J) node[right]{$J$} -- (N) node[right]{$N$};
    \\draw[dashed] (A) -- (B);
    \\draw[dashed] (I) -- (J);
    \\draw[dashed] (M) -- (N);
    \\draw[dashed] (S) -- (E) node[below]{$E$};
    \\fill (G) circle (1.5pt) node[above right]{$G$};
    \\fill (E) circle (1.5pt);
    \\end{tikzpicture}
    \\end{center}
    - Tìm giao tuyến $d$ của $(SAB)$ và $(GIJ)$:\\\\
    Dễ thấy $G \\in (SAB) \\cap (GIJ) \\Rightarrow G \\in d$ với $d = (SAB) \\cap (GIJ)$.\\\\
    $IJ$ là đường trung bình của hình thang $ABCD$ nên $IJ // AB$.\\\\
    Ta có: $\\begin{cases} d = (SAB) \\cap (GIJ) \\\\ AB // IJ \\\\ AB \\subset (SAB), IJ \\subset (GIJ) \\end{cases} \\Rightarrow d // AB // IJ$.\\\\
    Vậy giao tuyến $d$ của hai mặt phẳng $(SAB)$ và $(GIJ)$ là đường thẳng $d$ qua $G$ và song song với đường thẳng $AB$.\\\\
    - Tìm điều kiện của $AB$ và $CD$ để $MNJI$ là hình bình hành: Gọi $E$ là trung điểm $AB$.\\\\
    Ta có:\\\\
    $MN // IJ; MNJI$ là hình bình hành khi và chỉ khi $MN = IJ$. (1)\\\\
    Vì $MG // AE \\Rightarrow \\frac{SM}{SA} = \\frac{SG}{SE} = \\frac{%s}{%s}$ %s.\\\\
    Vì $MN // AB \\Rightarrow \\frac{MN}{AB} = \\frac{SM}{SA} = \\frac{%s}{%s} \\Rightarrow MN = \\frac{%s}{%s} AB$. (2)\\\\
    Vì $IJ$ là đường trung bình của hình thang $ABCD$ nên $IJ = \\frac{AB + CD}{2}$. (3)\\\\
    Từ (1), (2), (3), ta có:\\\\
    $\\frac{%s}{%s} AB = \\frac{AB + CD}{2} \\Leftrightarrow %s AB = %s AB + %s CD \\Leftrightarrow %s = %s CD \\Leftrightarrow AB = %s CD$.\\\\
    Suy ra với hình chóp ban đầu có $AB = %s CD$ thì $MNJI$ là hình bình hành.\\\\
    Vậy $k = %s$.'''
               % (latex(m), latex(n), reason_G,
                  latex(m), latex(n), latex(m), latex(n),
                  latex(m), latex(n), latex(2*m), latex(n), latex(n), v_2m_n_AB, latex(n), latex(k_val),
                  latex(k_val), latex(k_val)))
    dapan='\\shortans[0]{$%s$}\n'%(latex(k_val))
    # Xuất câu trắc nghiệm
    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n'+ str(noidungcauhoi)+ dapan+
               '\\loigiai{\n'+str(loigiai)+'\n}\n'
               '\\end{ex}\n\\end{minipage} \n\n')
    return content      

