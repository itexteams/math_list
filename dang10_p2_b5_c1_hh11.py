
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


def bt_dang10_p2_b5_c1_hh11(self):
    noidungcauhoi = ('''Cho hình hộp chữ nhật $ABCD.A'B'C'D'$. Xét các mệnh đề sau:''')
    nb_da_1 = 'Hình chiếu của $C$ lên $(A\'B\'C\')$ theo phương chiếu $DA\'$ trong phép chiếu song song là điểm $C\'$'
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''\\begin{center}
    \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,font=\\footnotesize,scale=1]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.5,-1);
    \\coordinate (D) at (3,0);
    \\coordinate (C) at ($(B)+(D)-(A)$);
    \\coordinate (A') at (0,-3);
    \\coordinate (B') at ($(A')+(B)-(A)$);
    \\coordinate (D') at ($(A')+(D)-(A)$);
    \\coordinate (C') at ($(B')+(D')-(A')$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (O') at ($(A')!0.5!(C')$);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (I') at ($(A')!0.5!(B')$);
    \\coordinate (G) at ($(C)!2/3!(I)$);
    \\coordinate (G') at ($(C')!2/3!(I')$);
    \\draw[line width=1pt] (B) -- (C) -- (D) -- (A) (B) -- (B') (A) -- (B) (C) -- (C') (D) -- (D') (A) -- (C) (B) -- (D) (B') -- (C') -- (D');
    \\draw[line width=1pt,dashed] (A) -- (D) (A) -- (A') (A') -- (B') (A') -- (D') (A') -- (C') (B') -- (D');
    \\draw[line width=1pt,dashed,red] (C) -- (B') (D) -- (A') (A) -- (A') (O) -- (O') (I) -- (I') (G) -- (G');
    \\fill (A) circle (1.5pt) node[above left] {$A$};
    \\fill (B) circle (1.5pt) node[left] {$B$};
    \\fill (C) circle (1.5pt) node[right] {$C$};
    \\fill (D) circle (1.5pt) node[right] {$D$};
    \\fill (A') circle (1.5pt) node[above right] {$A'$};
    \\fill (B') circle (1.5pt) node[below] {$B'$};
    \\fill (C') circle (1.5pt) node[right] {$C'$};
    \\fill (D') circle (1.5pt) node[right] {$D'$};
    \\fill (O) circle (1.5pt) node[above] {$O$};
    \\fill (O') circle (1.5pt) node[below] {$O'$};
    \\fill (I) circle (1.5pt) node[above left] {$I$};
    \\fill (I') circle (1.5pt) node[left] {$I'$};
    \\fill (G) circle (1.5pt) node[above] {$G$};
    \\fill (G') circle (1.5pt) node[below] {$G'$};
    \\end{tikzpicture}
    \\end{center}
    Do $\\begin{cases} B' \\in (A'B'C') \\\\ CB' \\parallel DA' \\end{cases}$ nên hình chiếu của $C$ lên $(A'B'C')$ là $B'$.''')
    list_nb_2 = [loigiai_nb_1]
    shuffled_answers_nb = list_nb_1
    shuffled_solutions_nb = list_nb_2
    th_da_1 = '\\True Gọi $O$ và $O\'$ lần lượt là tâm của $ABCD$ và $A\'B\'C\'D\'$. Hình chiếu của điểm $A$ lên mặt phẳng $(A\'B\'C\')$ theo phương chiếu $OO\'$ trong phép chiếu song song là điểm $A\'$'
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Do $\\begin{cases} A' \\in (A'B'C') \\\\ AA' \\parallel OO' \\end{cases}$ nên hình chiếu của $A$ lên mặt phẳng $(A'B'C')$ là $A'$.''')
    list_th_2 = [loigiai_th_1]
    shuffled_answers_th = list_th_1
    shuffled_solutions_th = list_th_2
    vd_da_1 = 'Gọi $I$ và $I\'$ lần lượt là trung điểm của $AB$ và $A\'B\'$. Hình chiếu của $I$ lên mặt phẳng $(A\'B\'C\')$ theo phương chiếu $AI\'$ trong phép chiếu song song là điểm $A\'$'
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Do $\\begin{cases} B' \\in (A'B'C') \\\\ IB' \\parallel AI' \\end{cases}$ nên hình chiếu của $I$ lên mặt phẳng $(A'B'C')$ là $B'$.''')
    list_vd_2 = [loigiai_vd_1]
    shuffled_answers_vd = list_vd_1
    shuffled_solutions_vd = list_vd_2
    vdc_da_1 = '\\True Gọi $G$ là trọng tâm $\\Delta ABC$. Gọi $G\'$ là hình chiếu của $G$ lên $(A\'B\'C\'D\')$ theo phương chiếu $II\'$ trong phép chiếu song song. Khi đó $G\'$ là trọng tâm $\\Delta A\'B\'C\'$'
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Ta có $I', G', C'$ lần lượt là ảnh của $I, G, C$ qua phép chiếu song song lên $(A'B'C'D')$ theo phương chiếu.
    Mặt khác $G$ là trọng tâm $\\Delta ABC$ nên $CG = \\dfrac{2}{3}CI$.
    Theo tính chất 3 thì $C'G' = \\dfrac{2}{3}C'I'$.
    Mà $I'$ là trung điểm $A'B'$.
    Nên $G'$ là trọng tâm $\\Delta A'B'C'$.''')
    list_vdc_2 = [loigiai_vdc_1]
    shuffled_answers_vdc = list_vdc_1
    shuffled_solutions_vdc = list_vdc_2
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
